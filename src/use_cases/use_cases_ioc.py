from bakery import Bakery, Cake

from src.use_cases.ohlc_reader import OHLCReader
from src.adapters.adapters_ioc import AdaptersIOC
from src.use_cases.securities_reader import SecuritiesReader
from src.use_cases.divid_reader import DividReader


class UseCasesIOC(Bakery):
    ohlc_reader: OHLCReader = Cake(
        OHLCReader,
        data_provider=AdaptersIOC.ohlc_provider,
    )

    securities_reader: SecuritiesReader = Cake(
        SecuritiesReader,
        data_provider=AdaptersIOC.securities_provider,
    )

    divid_reader: DividReader = Cake(
        DividReader,
        data_provider=AdaptersIOC.divi_provider,
    )
