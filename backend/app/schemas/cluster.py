from pydantic import BaseModel

class ClusterCreate(BaseModel):
    name: str

class ClusterOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
