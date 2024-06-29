from pydantic import BaseModel, Field, EmailStr


class RegisterInput(BaseModel):
    name: str
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=255)
    email: EmailStr


class LoginInput(BaseModel):
    username: str
    password: str
