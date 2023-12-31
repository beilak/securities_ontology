from fastapi import FastAPI
from src.adapters.adapters_ioc import AdaptersIOC
from src.use_cases.use_cases_ioc import UseCasesIOC
from src.api.ohlc.ohlc import ohlc_router


APP: FastAPI


async def service_startup() -> None:
    await AdaptersIOC.aopen()
    await UseCasesIOC.aopen()


async def service_shutdown() -> None:
    await AdaptersIOC.aclose()
    await UseCasesIOC.aclose()


_API_PREFIX = "/api"
APP = FastAPI(
    title="Securities data provider service",
    description="...",
    docs_url=f"{_API_PREFIX}/doc",
    on_startup=[service_startup],
    on_shutdown=[service_shutdown],
)

APP.include_router(ohlc_router, prefix=f"{_API_PREFIX }/ohlc", tags=["OHLC"])
