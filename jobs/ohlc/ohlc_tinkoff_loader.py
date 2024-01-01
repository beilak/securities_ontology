import asyncio
import os
from databases import Database
from datetime import datetime, timedelta
from tinkoff.invest import AsyncClient, CandleInterval
from tinkoff.invest.utils import now
from tinkoff.invest.services import MoneyValue
import decimal as dec
from tinkoff.invest.exceptions import AioRequestError, StatusCode


def conv_price_to_dec(price: MoneyValue):
    """Convert money from TF API to Decimal"""
    dec_money = dec.Decimal(price.units + price.nano / 10**9)
    return round(dec_money, 9)


async def fetch_ohlc_by_figi(
    figi: str,
    from_: datetime,
    interval: CandleInterval,
    api_token: str,
) -> list[dict]:
    ohlc: list[dict] = []

    async def __read_candles(candles) -> None:
        async for candle in candles:
            ohlc.append(
                {
                    "figi": figi,
                    "date_time": candle.time.replace(tzinfo=None),
                    "open": conv_price_to_dec(candle.open),
                    "high": conv_price_to_dec(candle.high),
                    "low": conv_price_to_dec(candle.low),
                    "close": conv_price_to_dec(candle.close),
                    "volume": candle.volume,
                }
            )

    async with AsyncClient(api_token) as client:
        candles = client.get_all_candles(
            figi=figi,
            from_=from_,
            interval=interval,
        )
        try:
            while True:
                await __read_candles(candles)
                break
        except AioRequestError as exc:
            if exc.code == StatusCode.RESOURCE_EXHAUSTED:
                print(exc.code)
                await asyncio.sleep(1)
            else:
                print(f"!!! Error {figi}", exc)

    return ohlc


async def fetch_figi(db: Database) -> set:
    query: str = """
        SELECT figi 
        FROM securities
        INNER JOIN exchange ON exchange.id = securities.exchange
        WHERE exchange.name in ('MOEX', 'SPB')
    """
    figis: set = set()
    for rec in await db.fetch_all(query):
        figis.add(rec["figi"])
    return figis


async def save_ohlc(ohlc, db) -> None:
    query = """
        INSERT INTO ohlc_1d (figi, date_time, open, high, low, close, volume)
        VALUES (:figi, :date_time, :open, :high, :low, :close, :volume)
        ON CONFLICT DO NOTHING
    """

    await db.execute_many(query=query, values=ohlc)


def calc_date_for_load(last_upload: datetime) -> datetime:
    delta_date = now().date() - last_upload.date()
    return now() - timedelta(days=delta_date.days)


async def fetch_last_upload_date(db: Database, figi) -> datetime:
    last_update_time = await db.fetch_val(
        "SELECT max(date_time) FROM ohlc_1d WHERE figi = :figi",
        values={"figi": figi},
    )
    if last_update_time:
        return last_update_time

    first_1day_candle_date = await db.fetch_val(
        "select first_1day_candle_date from securities where figi = :figi",
        values={"figi": figi},
    )
    if first_1day_candle_date:
        return datetime.combine(first_1day_candle_date, datetime.min.time())

    raise ValueError


async def main():
    db_dsn = os.getenv("DB_DSN", None)
    if not db_dsn:
        raise ValueError

    tinkoff_api_token = os.getenv("TINKOFF_API_TOKEN", None)
    if not tinkoff_api_token:
        raise ValueError

    database = Database(db_dsn)
    await database.connect()

    async def __run(figi) -> None:
        print(f"Processing {figi = } ...")

        last_update = await fetch_last_upload_date(db=database, figi=figi)
        date_for_load = calc_date_for_load(last_upload=last_update)

        ohlc = await fetch_ohlc_by_figi(
            figi=figi,
            from_=date_for_load,
            interval=CandleInterval.CANDLE_INTERVAL_DAY,
            api_token=tinkoff_api_token,
        )
        await save_ohlc(ohlc, database)
        print(f"Finish {figi = }!")

    tasks: set = set()
    for figi in await fetch_figi(db=database):
        tasks.add(__run(figi))

    await asyncio.gather(*tasks)


asyncio.run(main())
print("Done!")
