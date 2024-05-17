from sqlalchemy import Column, Integer, String
from db.database import Base
import hashlib

class UserDB(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    correo = Column(String, unique=True)
    numero_telefonico = Column(String)
    contraseña = Column(String)
    sexo = Column(String)
    edad = Column(Integer)
    peso = Column(Integer, nullable=True)
    estatura = Column(Integer, nullable=True)
    cedula_identidad = Column(String, unique=True)
    direccion = Column(String)
    fecha_nacimiento = Column(String)
    tipo_sangre = Column(String, nullable=True)

    def check_password(self, password: str) -> bool:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password == self.contraseña