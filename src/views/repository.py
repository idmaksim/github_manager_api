from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from schemas.repository import AddCollaborators, RepositoryCreate, RepositoryDetails
from services.github import GithubService
from views.dependencies import get_github_service


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
    """
    This method is used to create a new repository.
    Body: RepositoryCreate model (from schemas.repository)
    """
    await service.create_repo(repository)
    return {'message': 'repo created succesfully!'}


@router.delete("", status_code=status.HTTP_200_OK)
async def delete_repo(
    service: Annotated[GithubService, Depends(get_github_service)], 
    name: str
):
    """
    This method is used to delete a repository by name (Query param).
    """
    await service.delete_repo(name)
    return {'message': 'repo deleted succesfully!'}


@router.put("", status_code=status.HTTP_200_OK)
async def add_collaborators(
    service: Annotated[GithubService, Depends(get_github_service)],
    info: AddCollaborators
):
    """
    This method is used to add collaborators to a repository by name (Query param).
    Body: AddCollaborators model (from schemas.repository)
    """
    await service.add_collaborators(info.repo_name, info.usernames)
    return {'message': f'collaborators {info.usernames} added succesfully!'}


@router.delete("/all", status_code=status.HTTP_200_OK)
async def delete_all_repos(
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    This method is used to delete all repositories from the account.
    """
    await service.delete_all_repos()
    return {'message': 'all repos deleted succesfully!'}
  

@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_repos(
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    This method is used to get all repositories from the account.
    """
    repos_info = await service.get_all_repos()
    return repos_info


@router.get("/commits", status_code=status.HTTP_200_OK)
async def get_repo_commits(
    name: str,
    service: Annotated[GithubService, Depends(get_github_service)], 
):
    """
    This method is used to get the commit history of a repository by repo name.
    """
    commits = await service.get_commit_history(name)
    return commits


@router.get("/details", status_code=status.HTTP_200_OK, response_model=RepositoryDetails)
async def get_repo_details(
    name: str,
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    This method is used to get the details of a repository by repo name.
    """
    details = await service.get_repo_details(name)
    return details

