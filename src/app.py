from api.routers import main_api_router
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Github managerAPI",
    description="API for github manager",
    version="1.0"
)
app.include_router(main_api_router)


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def redirect_to_docs():
    return '/docs'
