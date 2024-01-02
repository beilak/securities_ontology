from bakery import Bakery, Cake
from databases import Database
from src.adapters.ohlc_provider import OhlcDbAdapter
from src.config import Config


class AdaptersIOC(Bakery):
    config: Config = Cake(
        Config,
    )

    db: Database = Cake(
        Cake(
            Database,
            config.DB_DSN,
        )
    )

    ohlc_provider: OhlcDbAdapter = Cake(
        OhlcDbAdapter,
        db=db,
    )
