"""Target and Target Cneter Router"""

from datetime import date, datetime, timedelta
from typing import List

from fastapi import APIRouter, status
from models.response_models import OHLCRespModel

ohlc_router: APIRouter = APIRouter()


@ohlc_router.get(
    "/{ticker}",
    status_code=status.HTTP_200_OK,
    response_model=List[OHLCRespModel],
)
async def ohlc_reader(
    ticker: str,
    date_from: date = datetime.today(),
    date_to: date = datetime.now() - timedelta(days=365),
) -> List[OHLCRespModel]:
    # ohls = await OHLCReader. e
    return
