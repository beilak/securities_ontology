from datetime import date, datetime, timedelta
from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import parse_obj_as
from src.api.ohlc.models.response_models import OHLCRespModel
from src.use_cases.models.enums import Candles
from src.use_cases.ohlc_reader import OHLCReader
from src.use_cases.use_cases_ioc import UseCasesIOC

ohlc_router: APIRouter = APIRouter()


@ohlc_router.get(
    "/{ticker}",
    status_code=status.HTTP_200_OK,
    response_model=List[OHLCRespModel],
)
async def ohlc_reader(
    ticker: str,
    date_from: date = datetime.now().date() - timedelta(days=365),
    date_to: date = datetime.today().date(),
    candles: Candles = Candles.DAY,
    use_case: OHLCReader = Depends(UseCasesIOC.ohlc_reader),
) -> List[OHLCRespModel]:
    return parse_obj_as(
        list[OHLCRespModel],
        await use_case.execute(
            ticker=ticker,
            candles=candles,
            from_=date_from,
            to_=date_to,
        ),
    )
