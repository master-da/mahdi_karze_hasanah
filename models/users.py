from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    user_name: str
    password: str
    first_name: str
    last_name: str
    email: str
    mobile_number: str
    date_of_birth: date
    address: str
    balance: float

class UserUpdate(BaseModel):
    user_name: Optional[str]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    mobile_number: Optional[str]
    date_of_birth: Optional[date]
    address: Optional[str]
    balance: Optional[float]

class PasswordReset(BaseModel):
    user_id: int
    new_password: str

class UserLogin(BaseModel):
    user_name: str
    password: str