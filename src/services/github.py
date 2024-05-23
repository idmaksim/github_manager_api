from github import Github, GithubException
from schemas.repository import RepositoryRequestModel


class GithubService:
    def __init__(self, access_token: str) -> None:
        self.github = Github(access_token)
        self.user = self.github.get_user()
        
    def delete_repo(self, repo_name: str) -> None:
        repo = self.user.get_repo(repo_name)
        
        if repo is None:
            raise GithubException(message='repo not found', status=404)
        
        repo.delete()
        
    def create_repo(self, repos: RepositoryRequestModel) -> None:
        self.user.create_repo(name=repos.name, description=repos.description, private=repos.private)
        
    def add_collaborators(self, repo_name: str, usernames: list[str]) -> None:
        repo = self.user.get_repo(repo_name)
        
        if repo is not None:
            for username in usernames:
                if username not in repo.get_collaborators():
                    repo.add_to_collaborators(username) 
        else:
            raise GithubException(message='repo not found', status=404)