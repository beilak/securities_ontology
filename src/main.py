from fastapi import FastAPI


APP: FastAPI


async def service_startup() -> None:
    ...


async def service_shutdown() -> None:
    ...


_API_PREFIX = "/api"
APP = FastAPI(
    title="Securities data provider service",
    description="...",
    # version=_API_VER,
    docs_url=f"{_API_PREFIX}/doc",
    on_startup=[service_startup],
    on_shutdown=[service_shutdown],
)


# FIN_APP.include_router(target_cnt_router, prefix=_API_PREFIX, tags=["Target"])
# FIN_APP.include_router(target_router, prefix=_API_PREFIX, tags=["Target flow"])
# FIN_APP.include_router(tech_router, prefix=_API_PREFIX, tags=["Tech"])
# FIN_APP.include_router(checker_router, prefix="/check", tags=["Check"])
