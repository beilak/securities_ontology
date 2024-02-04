from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import parse_obj_as
from src.api.info.models.response_models import SecuritiesRespModel
from src.use_cases.use_cases_ioc import UseCasesIOC
from src.use_cases.securities_reader import SecuritiesReader


securities_router: APIRouter = APIRouter()


@securities_router.get(
    "/securities",
    status_code=status.HTTP_200_OK,
    response_model=List[SecuritiesRespModel],
)
async def securities_reader(
    use_case: SecuritiesReader = Depends(UseCasesIOC.securities_reader),
) -> List[SecuritiesRespModel]:
    return parse_obj_as(
        list[SecuritiesRespModel],
        await use_case.execute(),
    )
