from typing import List
from pydantic import BaseModel


""" 
Classes for validation when receiving data from web requests
"""


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
