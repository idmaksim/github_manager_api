from views.repository import router as repository_router
from fastapi import APIRouter

main_api_router = APIRouter(
    prefix='/api'
)

routers = [
    repository_router,
]

[main_api_router.include_router(router) for router in routers]