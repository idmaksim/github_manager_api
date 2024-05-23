from github import Github, GithubException
from schemas.repository import RepositoryRequestModel


class GithubService:
    def __init__(self, access_token: str) -> None:
        self.github = Github(access_token)
        self.user = self.github.get_user()
        
    async def delete_repo(self, repo_name: str) -> None:
        repo = self.user.get_repo(repo_name)
        
        if repo is None:
            raise Exception('repo not found')
        
        repo.delete()
        
    async def create_repo(self, repo: RepositoryRequestModel) -> None:
        self.user.create_repo(name=repo.name, description=repo.description, private=repo.private)
        
    async def add_collaborators(self, repo_name: str, usernames: list[str]) -> None:
        repo = self.user.get_repo(repo_name)
        
        if repo is None:
            raise Exception('repo not found')
        
        for username in usernames:
            if username not in repo.get_collaborators():
                repo.add_to_collaborators(username) 

    async def delete_all_repos(self) -> None:
        repos = self.user.get_repos()
        if repos is None:
            raise Exception('repos not found')
        
        for repo in repos:
            repo.delete()