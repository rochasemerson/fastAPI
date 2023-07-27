from enum import IntEnum
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

class Token(BaseModel):
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class VoteEnum(IntEnum):
    UP = 1
    DOWN = 0

class Vote(BaseModel):
    post_id: int
    dir: VoteEnum