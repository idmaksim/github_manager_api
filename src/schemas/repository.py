from pydantic import BaseModel


class RepositoryRequestModel(BaseModel):
    name: str
    description: str
    private: bool = True
