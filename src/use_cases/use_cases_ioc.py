from bakery import Bakery, Cake

from use_cases.ohlc_reader import OHLCReader


class UseCasesIOC(Bakery):
    ohlc_reader: OHLCReader = Cake(
        OHLCReader,
        data_provider=None,
    )
