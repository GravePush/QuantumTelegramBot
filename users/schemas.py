from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: int
    username: str
    hashed_password: str


class UserIn(BaseModel):
    username: str = Field(min_length=2, max_length=32)
    password: str = Field(min_length=8, max_length=32)


class UserOut(BaseModel):
    id: int
    username: str


class UserResponseMessage(BaseModel):
    message: str
