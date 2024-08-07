from src.adapters.divid_provider import DividDbAdapter
from bakery import Bakery, Cake
from databases import Database
from src.adapters.ohlc_provider import OhlcDbAdapter
from src.adapters.securities_provider import SecuritiesDbAdapter
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

    securities_provider: SecuritiesDbAdapter = Cake(
        SecuritiesDbAdapter,
        db=db,
    )

    divi_provider = Cake(
        DividDbAdapter,
        db=db,
    )
