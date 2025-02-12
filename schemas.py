from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    student = "student"
    faculty = "faculty"
    contributor = "contributor"

class UserCreate(BaseModel):
    username: str
    password: str
    role: UserRole
    email: EmailStr


class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: str

class AssignmentCreate(BaseModel):
    title: str

class FeedbackRequest(BaseModel):
    feedback: str
