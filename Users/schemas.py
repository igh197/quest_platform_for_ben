from pydantic import BaseModel
from pydantic import validator


class UserCreate(BaseModel):
    user_id: int
    user_name: str
    password: str
    gold: int
    diamond: int
    status: int
    login_trial: int


class UserLogin(BaseModel):
    user_name: str
    password: str


class UserRead(BaseModel):
    id: int
    user_name: str
    gold: int
    diamond: int
    status: int
    login_trial: int

    class Config:
        orm_mode = True
