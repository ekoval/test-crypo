from pydantic import BaseModel


class DataSchema(BaseModel):
    data: dict

    class Config:
        orm_mode = True


class PortfolioSchema(BaseModel):
    username: str
    data: dict

    class Config:
        orm_mode = True
