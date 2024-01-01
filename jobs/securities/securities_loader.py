import os
from sqlalchemy.util import asyncio

from tinkoff.invest import Client, ShareResponse, Share
from tinkoff.invest.services import InstrumentsService

from databases import Database


def fetch_shares_info(
    token: str,
):
    """Fatching tickers info"""

    with Client(token) as client:
        instruments: InstrumentsService = client.instruments

        shares: ShareResponse = instruments.shares()
        return shares.instruments


async def save_data(values: list[dict]):
    db_dsn = os.getenv("DB_DSN", None)
    database = Database(db_dsn)

    await database.connect()
    query = """
        INSERT INTO securities(figi, ticker, name, ipo_date, first_1day_candle_date, currency, exchange)
        VALUES (:figi, :ticker, :name, :ipo_date, :first_1day_candle_date, :currency, :exchange)
        ON CONFLICT (figi) DO UPDATE
        SET 
            name = :name,
            ipo_date = :ipo_date,
            first_1day_candle_date = :first_1day_candle_date
    """

    await database.execute_many(query=query, values=values)

    await database.disconnect()


def load_data() -> None:
    tinkoff_api_token = os.getenv("TINKOFF_API_TOKEN", None)
    if not tinkoff_api_token:
        raise ValueError

    shares = fetch_shares_info(token=tinkoff_api_token)
    share: Share

    securities: [dict] = []
    for share in shares:
        securities.append(
            {
                "figi": share.figi,
                "name": share.name,
                "ticker": share.ticker,
                "ipo_date": share.ipo_date,
                "first_1day_candle_date": share.first_1day_candle_date,
                "currency": share.currency.upper(),
                "exchange": share.exchange.upper(),
            }
        )
    return securities


def main() -> None:
    securities_data = load_data()
    asyncio.run(
        save_data(securities_data),
    )


main()
