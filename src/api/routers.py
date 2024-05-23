from fastapi import APIRouter

from api import repository, letshack_info


main_api_router = APIRouter(
    prefix='/api'
)

routers = [
    repository.router,
    letshack_info.router
]

[main_api_router.include_router(router) for router in routers]