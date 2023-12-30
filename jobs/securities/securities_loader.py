import os
from sqlalchemy.util import asyncio

from tinkoff.invest import Client, ShareResponse, Share
from tinkoff.invest.services import InstrumentsService

from databases import Database

# from datetime import timedelta, datetime


# LOAD_SHARE_DATE_FROM = now() - timedelta(days=30 * 12)
# LOAD_CURRENCY_DATE_FROM = now() - timedelta(days=30 * 12)

# CANDLE_INTERVAL = CandleInterval.CANDLE_INTERVAL_1_MIN

# CANDLE_INTERVAL = CandleInterval.CANDLE_INTERVAL_HOUR


# SHARES_FOR_LOAD = {"SBER", "YNDX"}


def fetch_shares_info(
    token: str,  # shares_filter: ShareInfoFilter
):  # -> dict[TickerID, Share]:
    """Fatching tickers info"""

    with Client(token) as client:
        instruments: InstrumentsService = client.instruments
        # share_catalog: dict[TickerID, Share] = {}

        shares: ShareResponse = instruments.shares()
        return shares.instruments
        # share: Share
        # for share in shares:
        #     # if not _is_share_pass_filter(share=share, shares_filter=shares_filter):
        #     #   continue
        #
        #     share_catalog[share.ticker] = share
        #
        # return share_catalog


async def save_data(values: list[dict]):
    db_dsn = os.getenv("DB_DSN", None)
    database = Database(db_dsn)

    await database.connect()
    query = """
        INSERT INTO securities(figi, ticker, name, currency, exchange)
        VALUES (:figi, :ticker, :name, :currency, :exchange)
        ON CONFLICT DO NOTHING
    """

    await database.execute_many(query=query, values=values)

    # Close all connections in the connection pool
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
