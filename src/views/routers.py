from views.repository import router as repository_router
from fastapi import APIRouter


main_api_router = APIRouter(
    prefix='/api'
)

# list of routers from the views
routers = [
    repository_router,
]

# including views routers to main router
[main_api_router.include_router(router) for router in routers]