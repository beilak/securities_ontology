from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import parse_obj_as
from src.api.info.models.response_models import Exchanges, SecuritiesRespModel
from src.use_cases.use_cases_ioc import UseCasesIOC
from src.use_cases.securities_reader import SecuritiesReader
from tinkoff.invest import ShareType
from datetime import date

securities_router: APIRouter = APIRouter()


@securities_router.get(
    "/securities",
    status_code=status.HTTP_200_OK,
    response_model=List[SecuritiesRespModel],
)
async def securities_reader(
    securities_type: ShareType,
    exchange: Exchanges,
    first_1d_candle: date = date.today(),
    use_case: SecuritiesReader = Depends(UseCasesIOC.securities_reader),
) -> List[SecuritiesRespModel]:
    return parse_obj_as(
        list[SecuritiesRespModel],
        await use_case.execute(
            securities_type=securities_type,
            exchange=exchange,
            first_1d_candle=first_1d_candle,
        ),
    )
