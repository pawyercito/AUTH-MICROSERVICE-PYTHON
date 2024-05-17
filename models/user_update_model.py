# models/user_model.py
from pydantic import BaseModel
from typing import Optional

class UserUpdateModel(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo: Optional[str] = None
    numero_telefonico: Optional[str] = None
    sexo: Optional[str] = None
    edad: Optional[int] = None
    peso: Optional[int] = None
    estatura: Optional[int] = None
    cedula_identidad: Optional[str] = None
    direccion: Optional[str] = None
    fecha_nacimiento: Optional[str] = None
    tipo_sangre: Optional[str] = None