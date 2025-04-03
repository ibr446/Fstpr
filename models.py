from wsgiref.validate import validator

from pydantic import BaseModel
from typing import Optional
from service import PasswordService



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
