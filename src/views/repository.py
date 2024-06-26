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


async def add_repo(
    repository: RepositoryCreate,
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """    
    Create a new repository route.    
    Args:
        repository (RepositoryCreate): A model containing the data for the new repository.
        service (Annotated[GithubService, Depends(get_github_service)]): An instance of the GithubService class.

    Returns:
        dict: A dictionary containing a success message
    """
    await service.create_repo(repository)
    return {'message': 'repo created succesfully!'}



@router.delete("", status_code=status.HTTP_200_OK)
async def delete_repo(
    service: Annotated[GithubService, Depends(get_github_service)], 
    name: str
):  
    """
    Delete a repository route.    
    Args
        service (Annotated[GithubService, Depends(get_github_service)]): An instance of the GithubService class.
        name (str): The name of the repository to delete.

    Returns:
        dict: A dictionary containing a success message.
    """
    await service.delete_repo(name)
    return {'message': 'repo deleted succesfully!'}


@router.put("", status_code=status.HTTP_200_OK)
async def add_collaborator(
    service: Annotated[GithubService, Depends(get_github_service)],
    info: AddCollaborators
):
    """    
    Add a collaborator to a repository route.    
    Args:
        service (Annotated[GithubService, Depends(get_github_service)]): An instance of the GithubService class.
        info (AddCollaborators): A model containing the repository name and usernames of the collaborators to add.

    Returns:
        dict: dictionary containing a success message.
    """
    await service.add_collaborators(info.repo_name, info.usernames)
    return {'message': f'collaborators {info.usernames} added succesfully!'}


@router.delete("/all", status_code=status.HTTP_200_OK)
async def delete_all_repos(
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    Delete all repositories route.    
    Args:
        service (Annotated[GithubService, Depends(get_github_service)]): An instance of the GithubService class.
    """
    await service.delete_all_repos()
    return {'message': 'all repos deleted succesfully!'}
  

@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_repos(
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    Get all repositories route.    
    Args:
        service (Annotated[GithubService, Depends(get_github_service)]): An instance of the GithubService class.

    Returns:
        list: A list of all repositories.
    """
    repos_info = await service.get_all_repos()
    return repos_info


@router.get("/commits", status_code=status.HTTP_200_OK)
async def get_repo_commits(
    name: str,
    service: Annotated[GithubService, Depends(get_github_service)], 
):
    """
    Get commits history of a repository route.    
    Args:
        name (str): The name of the repository to get commit history for.
        service (Annotated[GithubService, Depends(get_github_service)]): An instance of the GithubService class.

    Returns:
        list: A list of commit history for the repository
    """
    commits = await service.get_commit_history(name)
    return commits


@router.get("/details", status_code=status.HTTP_200_OK, response_model=RepositoryDetails)
async def get_repo_details(
    name: str,
    service: Annotated[GithubService, Depends(get_github_service)],
):
    """
    Get details of a repository route.    
    Args:
        name (str): The name of the repository to get details for.
        service (Annotated[GithubService, Depends(get_github_service)]): An instance of the GithubService class.

    Returns:
        RepositoryDetails: The of the repository.
    """
    details = await service.get_repo_details(name)
    return details
