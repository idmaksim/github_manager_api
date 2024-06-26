from fastapi import HTTPException, Request
from services.github import GithubService


def get_github_service(request: Request):
    """
    This method returns a GithubService instance if access-token is not missing.
    """
    access_token = request.headers.get('access-token')
    if not access_token:
        raise HTTPException(status_code=400, detail="Access token is missing")
    return GithubService(access_token)
