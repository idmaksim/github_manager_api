from fastapi import Request, HTTPException
from services.github import GithubService

def get_github_service(request: Request):
    access_token = request.headers.get('access-token')
    if not access_token:
        raise HTTPException(status_code=400, detail="Access token is missing")
    return GithubService(access_token)
