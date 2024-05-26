from typing import Annotated, List

from api.dependencies import get_github_service
from fastapi import APIRouter, Depends, Response, status
from schemas.repository import RepositoryRequestModel
from services.github import GithubService
from utils.error_handler import handle_route_error

router = APIRouter(
    prefix="/repos",
    tags=["Repository"],
)


@router.post("")
async def add_repo(
    repository: RepositoryRequestModel,
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    return HTTP_201_CREATED if repo created successfully

    Args:
        repository (RepositoryRequestModel): _description_
        service (Annotated[GithubService, Depends): _description_

    Returns:
        none: only status code is returned
    """
    try:
        await service.create_repo(repository)
        return Response(status_code=status.HTTP_201_CREATED)

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_400_BAD_REQUEST)


@router.delete("")
async def delete_repo(
    service: Annotated[GithubService, Depends(get_github_service)], name: str
):
    """
    return HTTP_200_OK if repo deleted successfully

    Args:
        service (Annotated[GithubService, Depends): depends on github service
        name (str): name of the repo

    Returns:
        none: only status code is returned
    """
    try:
        await service.delete_repo(name)
        return Response(status_code=status.HTTP_200_OK)

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_404_NOT_FOUND)


@router.put("")
async def add_collaborators(
    service: Annotated[GithubService, Depends(get_github_service)],
    repo_name: str,
    usernames: List[str],
):
    """
    return HTTP_200_OK if collaborators added successfully

    Args:
        service (Annotated[GithubService, Depends): depepends on github service
        repo_name (str): name of the repo
        usernames (List[str]): collaborators to add

    Returns:
        none: only status code is returned
    """
    try:
        await service.add_collaborators(repo_name, usernames)
        return Response(status_code=status.HTTP_200_OK)

    except Exception as e:
        await handle_route_error(e, status.HTTP_304_NOT_MODIFIED)


@router.delete("/all")
async def delete_all_repos(
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    return HTTP_200_OK if repos deleted successfully

    Args:
        service (Annotated[GithubService, Depends): depends on github service

    Returns:
        none: only status code is returned
    """
    try:
        await service.delete_all_repos()
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/all")
async def get_all_repos(
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    returns list of all repos

    Args:
        service (Annotated[GithubService, Depends): depends on github service

    Returns:
        list: list of dict info of repos
    """
    try:
        repos_info = await service.get_all_repos()
        return repos_info

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_404_NOT_FOUND)


@router.get("/commits")
async def get_repo_commits(
    service: Annotated[GithubService, Depends(get_github_service)], name: str
):
    """
    returns commit history of a repo

    Args:
        service (Annotated[GithubService, Depends): depends on github service
        name (str): name of the repo

    Returns:
        list: list of dict info of commits
    """
    try:
        commits = await service.get_commit_history(name)
        return commits

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_404_NOT_FOUND)


@router.get("/details")
async def get_repo_details(
    name: str,
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    returns details of a repo

    Args:
        name (str): name of the repo
        service (Annotated[GithubService, Depends): depends on github service

    Returns:
        list: list of dict info of commits
    """
    try:
        details = await service.get_repo_details(name)
        return details

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_404_NOT_FOUND)
