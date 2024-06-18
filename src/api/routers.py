from api import repository
from fastapi import APIRouter

main_api_router = APIRouter(
    prefix='/api'
)

routers = [
    repository.router,
]

[main_api_router.include_router(router) for router in routers]