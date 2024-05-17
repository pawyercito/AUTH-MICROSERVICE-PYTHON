# models/login_dto.py
from pydantic import BaseModel

class LoginDTO(BaseModel):
    correo: str
    contraseña: str