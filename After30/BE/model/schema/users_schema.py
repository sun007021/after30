from pydantic import BaseModel, field_validator
from datetime import date
from dataclasses import dataclass
from typing import Optional


class Users(BaseModel):
    _id: Optional[str] = None
    email: str
    password: str
    name: str
    sex: str
    birth: date
    phone: str

    @field_validator('sex')
    def sex_validator(cls, v):
        if v not in ('M', 'W'):
            raise ValueError(
                'sex must be one of M, W')
        return v

    class Config:
        from_attributes = True


class UserCreated(BaseModel):
    """User Create Model(Output)"""
    email: str


class UserGet(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
