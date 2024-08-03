import os

from databases import Database
from sqlalchemy.util import asyncio
from tinkoff.invest import Client, CurrenciesResponse, Currency, Share, ShareResponse
from tinkoff.invest.services import InstrumentsService


def fetch_shares_info(
    token: str,
):
    """Fatching tickers info"""

    with Client(token) as client:
        instruments: InstrumentsService = client.instruments

        shares: ShareResponse = instruments.shares()
        return shares.instruments


def fetch_currencies_info(
    token: str,
) -> list[Currency]:
    with Client(token) as client:
        instruments: InstrumentsService = client.instruments

        currencies: CurrenciesResponse = instruments.currencies()
        return currencies.instruments


async def save_data(values: list[dict]):
    db_dsn = os.getenv("DB_DSN", None)
    database = Database(db_dsn)

    await database.connect()
    query = """
        INSERT INTO securities(figi, ticker, name, ipo_date, first_1day_candle_date, currency, exchange, securities_type)
        VALUES (:figi, :ticker, :name, :ipo_date, :first_1day_candle_date, :currency, :exchange, :securities_type)
        ON CONFLICT (figi) DO UPDATE
        SET 
            name = :name,
            ipo_date = :ipo_date,
            first_1day_candle_date = :first_1day_candle_date,
            securities_type = :securities_type
    """
    # print(set([i["exchange"] for i in values]))
    await database.execute_many(query=query, values=values)

    await database.disconnect()


def load_data() -> list[dict]:
    tinkoff_api_token = os.getenv("TINKOFF_API_TOKEN", None)
    if not tinkoff_api_token:
        raise ValueError("TINKOFF_API_TOKEN")

    shares = fetch_shares_info(token=tinkoff_api_token)

    currencies: list[Currency] = fetch_currencies_info(token=tinkoff_api_token)
    # share: Share

    # securities: [dict] = []
    # collect_securities

    def collect_securities(instruments: list[Currency] | list[Share]) -> list[dict]:
        securities: [dict] = []
        for instrument in instruments:
            if isinstance(instrument, Share):
                ipo_date = instrument.ipo_date
                share_type = instrument.share_type.value
            else:
                ipo_date = instrument.first_1day_candle_date
                share_type = 0

            securities.append(
                {
                    "figi": instrument.figi,
                    "name": instrument.name,
                    "ticker": instrument.ticker,
                    "ipo_date": ipo_date,
                    "first_1day_candle_date": instrument.first_1day_candle_date,
                    "currency": instrument.currency.upper(),
                    "exchange": instrument.exchange.upper(),
                    "securities_type": share_type,
                }
            )
        return securities

    return collect_securities(shares) + collect_securities(currencies)


def main() -> None:
    securities_data = load_data()
    asyncio.run(
        save_data(securities_data),
    )


main()
