from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from schemas.repository import AddCollaborators, RepositoryCreate
from services.github import GithubService
from api.dependencies import get_github_service


router = APIRouter(
    prefix="/repos",
    tags=["Repository"],
    default_response_class=JSONResponse
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_repo(
    repository: RepositoryCreate,
    service: Annotated[GithubService, Depends(get_github_service)],
):
    await service.create_repo(repository)
    return {'message': 'repo created succesfully!'}


@router.delete("", status_code=status.HTTP_200_OK)
async def delete_repo(
    service: Annotated[GithubService, Depends(get_github_service)], 
    name: str
):
    await service.delete_repo(name)
    return {'message': 'repo deleted succesfully!'}


@router.put("", status_code=status.HTTP_200_OK)
async def add_collaborators(
    service: Annotated[GithubService, Depends(get_github_service)],
    info: AddCollaborators
):
    await service.add_collaborators(info.repo_name, info.usernames)
    return {'message': f'collaborators {info.usernames} added succesfully!'}


@router.delete("/all", status_code=status.HTTP_200_OK)
async def delete_all_repos(
    service: Annotated[GithubService, Depends(get_github_service)],
):
    await service.delete_all_repos()
    return {'message': 'all repos deleted succesfully!'}
  

@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_repos(
    service: Annotated[GithubService, Depends(get_github_service)],
):
    repos_info = await service.get_all_repos()
    return repos_info


@router.get("/commits", status_code=status.HTTP_200_OK)
async def get_repo_commits(
    name: str,
    service: Annotated[GithubService, Depends(get_github_service)], 
):
    commits = await service.get_commit_history(name)
    return commits


@router.get("/details", status_code=status.HTTP_200_OK)
async def get_repo_details(
    name: str,
    service: Annotated[GithubService, Depends(get_github_service)],
):
    details = await service.get_repo_details(name)
    return details

