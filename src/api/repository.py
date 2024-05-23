from typing import Annotated
from fastapi import Depends, Request, Response, APIRouter, status
from api.dependencies import get_github_service
from schemas.repository import RepositoryRequestModel
from services.github import GithubService
from utils.error_handler import handle_route_error


router = APIRouter(
    prefix="/repos",
    tags=["Repository"],
)


@router.post('')
async def add_repo(
    repository: RepositoryRequestModel,
    service: Annotated[GithubService, Depends(get_github_service)],
):
    try:
        service.create_repo(repository)
        return Response(status_code=200)
    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_400_BAD_REQUEST)
        

@router.delete('')
async def delete_repo(
    service: Annotated[GithubService, Depends(get_github_service)],
    name: str
):
    try:
        service.delete_repo(name)
        return Response(status_code=200)
    
    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_404_NOT_FOUND)


@router.put('')
async def add_collaborators(
    request: Request,
    service: Annotated[GithubService, Depends(get_github_service)],
    name: str
):
    try:
        user_names: list[str] = (await request.json())['user_names']
        
        service.add_collaborators(name, user_names)

        return Response(status_code=200)
    
    except Exception as e:
        await handle_route_error(e, status.HTTP_304_NOT_MODIFIED)