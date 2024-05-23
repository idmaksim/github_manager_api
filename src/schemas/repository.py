from pydantic import BaseModel, Field


class RepositoryAdd(BaseModel):
    name: str
    description: str
    private: bool = True
