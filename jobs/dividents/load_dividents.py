from datetime import date, datetime
from logging import exception
import os
import time

import decimal as dec
from typing import Generator
from tinkoff.invest.exceptions import RequestError
from tinkoff.invest.services import MoneyValue
from databases import Database
from sqlalchemy.util import asyncio
from tinkoff.invest import (
    Client,
    CurrenciesResponse,
    Currency,
    Dividend,
    GetDividendsResponse,
    Share,
    ShareResponse,
)
from tinkoff.invest.services import InstrumentsService

DIV_LOAD_FROM_ = datetime(1991, 1, 1)


def conv_price_to_dec(price: MoneyValue):
    """Convert money from TF API to Decimal"""
    dec_money = dec.Decimal(price.units + price.nano / 10**9)
    return round(dec_money, 9)


def fetch_shares_info(client) -> Generator:
    """Fatching tickers info"""
    instruments: InstrumentsService = client.instruments
    shares: ShareResponse = instruments.shares()
    for share in shares.instruments:
        yield share


def fetch_divs(client, figi) -> list[Dividend]:
    instruments: InstrumentsService = client.instruments
    try:
        divid: GetDividendsResponse = instruments.get_dividends(
            figi=figi,
            from_=DIV_LOAD_FROM_,
            to=datetime.now(),
        )
        if divid.dividends is None:
            return []
        return divid.dividends
    except RequestError as e:
        print(f"ERROR {e}")
        time.sleep(61)
    return []


async def save_data(values: list[dict]):
    db_dsn = os.getenv("DB_DSN", None)
    database = Database(db_dsn)

    await database.connect()
    query = """
        INSERT INTO divid(figi, declared_date, last_buy_date, payment_date, dividend_net)
        VALUES (:figi, :declared_date, :last_buy_date, :payment_date, :dividend_net)
        ON CONFLICT (figi, declared_date, last_buy_date, payment_date) DO UPDATE
        SET 
            dividend_net = :dividend_net
    """
    await database.execute_many(query=query, values=values)

    await database.disconnect()


def load_and_save_data() -> list[dict]:
    tinkoff_api_token = os.getenv("TINKOFF_API_TOKEN", None)
    if not tinkoff_api_token:
        raise ValueError("TINKOFF_API_TOKEN")

    divs: list[Dividend]

    with Client(tinkoff_api_token) as client:
        shares: Generator = fetch_shares_info(client)
        for share in shares:
            print(f"Processing { share.figi}")
            divs = fetch_divs(client, figi=share.figi)
            if divs:
                asyncio.run(
                    save_data(
                        [
                            {
                                "figi": share.figi,
                                "dividend_net": conv_price_to_dec(i.dividend_net),
                                "declared_date": i.declared_date.replace(tzinfo=None),
                                "payment_date": i.payment_date.replace(tzinfo=None),
                                "last_buy_date": i.last_buy_date.replace(tzinfo=None),
                            }
                            for i in divs
                        ]
                    ),
                )


def main() -> None:
    load_and_save_data()


main()
