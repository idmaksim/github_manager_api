from views.routers import main_api_router
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

"""
Full documentation you can see at [server_ip_address:port]/docs or /redoc
"""

app = FastAPI(
    title="Github manager API",
    description="API for github manager",
    version="1.0"
)
app.include_router(main_api_router)


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def redirect_to_docs():
    """
    This function is a route handler for the root path of the application. 
    It redirects the user to the documentation page.

    return: A string containing the path to the documentation page.
    :rtype: str
    """
    return '/docs'
