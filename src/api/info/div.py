from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import parse_obj_as
from src.api.info.models.response_models import (
    DividensRespModel,
    DviRespModel,
    Exchanges,
    SecuritiesRespModel,
)
from src.use_cases.use_cases_ioc import UseCasesIOC
from src.use_cases.securities_reader import SecuritiesReader
from tinkoff.invest import ShareType
from datetime import date

from src.use_cases.divid_reader import DividReader

div_router: APIRouter = APIRouter()


@div_router.get(
    "/divs",
    status_code=status.HTTP_200_OK,
    response_model=DividensRespModel,
)
async def divs_reader(
    ticker: str,
    use_case: DividReader = Depends(UseCasesIOC.divid_reader),
) -> DividensRespModel:
    divs = await use_case.execute(
        ticker=ticker.upper(),
    )

    return DividensRespModel(
        figi=divs["figi"],
        ticker=divs["ticker"],
        div=parse_obj_as(
            list[DviRespModel],
            divs["div"],
        ),
    )
