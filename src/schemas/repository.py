from typing import List
from pydantic import BaseModel


class RepositoryCreate(BaseModel):
    name: str
    description: str
    private: bool = True


class AddCollaborators(BaseModel):
    repo_name: str
    usernames: List[str]


class RepositoryDetails(BaseModel):
    name: str
    description: str
    private: bool
    collaborators: list[str]
    branches: list 
    releases: list
