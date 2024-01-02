from bakery import Bakery, Cake

from src.use_cases.ohlc_reader import OHLCReader
from src.adapters.adapters_ioc import AdaptersIOC


class UseCasesIOC(Bakery):
    ohlc_reader: OHLCReader = Cake(
        OHLCReader,
        data_provider=AdaptersIOC.ohlc_provider,
    )
