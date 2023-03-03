from pydantic import BaseModel


class DemoBase(BaseModel):
    id: int
    number: int
    password: int

    class Config:
        orm_mode = True
