# models/login_response.py
from pydantic import BaseModel
from typing import Optional
from models.login_model_dto import LoginDTO

class LoginResponse(BaseModel):
    message: str
    status_code: int
    correo: str
    token: str