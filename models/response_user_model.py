from pydantic import BaseModel
from typing import Optional

class ResponseModel(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: str
    numero_telefonico: Optional[str] = None
    sexo: str
    edad: int
    peso: Optional[int] = None
    estatura: Optional[int] = None
    cedula_identidad: str
    direccion: str
    fecha_nacimiento: str
    tipo_sangre: Optional[str] = None
    message: str
    status_code: int
