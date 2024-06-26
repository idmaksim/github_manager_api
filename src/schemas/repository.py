from typing import List
from pydantic import BaseModel

# TODO comment file bopleromn

class RepositoryCreate(BaseModel):
    name: str
    description: str
    private: bool = True


class AddCollaborators(BaseModel):
    repo_name: str
    usernames: List[str]


class RepositoryDetails(BaseModel):
    name: str
    description: str | None
    private: bool
    collaborators: list
    branches: list 
    releases: list
