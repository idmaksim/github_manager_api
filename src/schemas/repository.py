from typing import List
from pydantic import BaseModel


""" 
Classes for validation when receiving data from web requests
"""


class RepositoryCreate(BaseModel): 
    """
    A class to represent a repository to be created.

    Attributes:
        name (str): The name of the repository.
        description (str): The description of the repository.
        private (bool): the repository is private (default: True).
    """
    name: str
    description: str
    private: bool = True


class AddCollaborators(BaseModel):
    """
    A class to represent the collaborators to be added to a repository.

    Attributes:
        repo_name (str): The name of the repository.
        usernames (List[str]): A list of usernames to add as collaborators.
    """
    repo_name: str
    usernames: List[str]


class RepositoryDetails(BaseModel):
    """
    A class to represent the details of a repository.

    Attributes:
        name (str): The name of the repository.
        description (str | None): The description of the repository.
        private (): Whether the repository is private.
        collaborators (list): A list of collaborators for the repository.
        branches (list): A list of branches for the repository.
        releases (list): A list of releases for the repository.
    """
    name: str
    description: str | None
    private: bool
    collaborators: list
    branches: list 
    releases: list
