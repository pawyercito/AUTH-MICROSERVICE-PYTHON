from pydantic import BaseModel
from typing import Optional

class UserDTO(BaseModel):
    nombre: str
    apellido: str
    correo: str
    numero_telefonico: Optional[str] = None
    contraseña: str
    sexo: str
    edad: int
    peso: Optional[int] = None
    estatura: Optional[int] = None
    cedula_identidad: str
    direccion: str
    fecha_nacimiento: str
    tipo_sangre: Optional[str] = None


# Path: models/user_model.py