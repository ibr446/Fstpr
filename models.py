from pydantic import BaseModel

class User(BaseModel):
    id: int
    fullname: str
    username: str
    email: str
    password: str


class BaseResponse(BaseModel):
    status: bool
    body: str | list | dict | None = None
    error: str | None = None
