from pydantic import BaseModel, Field


class RepositoryRequestModel(BaseModel):
    name: str
    description: str
    private: bool = True
