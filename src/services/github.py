from fastapi import HTTPException, status
from github import Github

from github.GithubException import (
    UnknownObjectException,
    GithubException
)
from schemas.repository import RepositoryCreate


class GithubService:
    def __init__(self, access_token: str) -> None:
        self.github = Github(access_token)
        self.user = self.github.get_user()
        
    async def delete_repo(self, repo_name: str) -> None:
        try:
            repo = self.user.get_repo(repo_name)
            if repo is None:
                raise HTTPException(
                    detail='repo not found', 
                    status_code=status.HTTP_404_NOT_FOUND
                )
            repo.delete()
            
        except UnknownObjectException:
            raise HTTPException(
                detail='repo not found',
                status_code=status.HTTP_404_NOT_FOUND
            )
        
    async def create_repo(self, repo: RepositoryCreate) -> None:
        try:

            new_repo = self.user.create_repo(
                name=repo.name, 
                description=repo.description, 
                private=repo.private
            )
            if new_repo is None:
                raise HTTPException(
                    detail='repo not created',
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR 
                )
        except GithubException:
            raise HTTPException(
                detail='repo already exists',
                status_code=status.HTTP_409_CONFLICT 
            )


    async def add_collaborators(self, repo_name: str, usernames: list[str]) -> None:
        repo = self.user.get_repo(repo_name)
        if repo is None:
            raise HTTPException(
                detail='repo not found', 
                status_code=status.HTTP_404_NOT_FOUND
            )
        for username in usernames:
            if username not in repo.get_collaborators():
                repo.add_to_collaborators(username) 

    async def delete_all_repos(self) -> None:
        repos = self.user.get_repos()
        if repos is None:
            raise HTTPException(
                detail='repos not found', 
                status_code=status.HTTP_404_NOT_FOUND
            )
        for repo in repos:
            repo.delete()

    async def get_all_repos(self):
        repos = self.user.get_repos()
        dict_repos = [
            dict(
                name=repo.name, 
                description=repo.description, 
                private=repo.private
            ) 
            for repo in repos
        ]

        if dict_repos:
            return dict_repos
        raise HTTPException(
            detail='repos not found', 
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    async def get_repo_details(self, repo_name: str):
        repo = self.user.get_repo(repo_name)
        if repo is None:
            raise HTTPException(
                detail='repo not found', 
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        details = {
            'name': repo.name,
            'description': repo.description,
            'private': repo.private,
            'collaborators': [collaborator.login for collaborator in repo.get_collaborators()],
            'branches': [branch.name for branch in repo.get_branches()],
            'releases': [release.title for release in repo.get_releases()],
        }
        
        return details
    
    async def get_commit_history(self, name: str):
        repo = self.user.get_repo(name)
        
        if repo is None:
            raise HTTPException(
                detail='repo not found', 
                status_code=status.HTTP_404_NOT_FOUND
            )
        commits = repo.get_commits()
        
        return [
            {
                'sha': commit.sha,
                'message': commit.commit.message,
                'author': commit.author.login,
                'date': commit.commit.author.date
            }
            for commit in commits
        ]
                        

        
                