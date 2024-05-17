from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from use_case.login_use_case import LoginUseCase
from models.login_model_dto import LoginDTO
from models.login_response_model import LoginResponse
from repositories.login_repository import UserRepository
from db.database import get_db
from pydantic import ValidationError
from utils.generate_login_token import create_access_token
from utils.generate_login_token import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta


router = APIRouter()

@router.post("/login/", response_model=LoginResponse)
def login_user(login_dto: LoginDTO, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    login_use_case = LoginUseCase(user_repository)
    try:
        user = login_use_case.login_user(login_dto)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail="Datos de solicitud inválidos.")
    
    # Generar el token de acceso
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.correo}, expires_delta=access_token_expires
    )
    
    # Asegúrate de proporcionar valores para todos los campos requeridos en LoginResponse
    return LoginResponse(message="Inicio de sesión exitoso", status_code=200, correo=user.correo, token=access_token)