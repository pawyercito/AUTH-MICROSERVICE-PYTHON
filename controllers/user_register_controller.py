# controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from use_case.user_use_case import UserUseCase
from models.user_model_dto import UserDTO
from models.user_response import UserOut
from db.database import get_db
from repositories.user_repository import UserRepository
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from models.response_user_model import ResponseModel
from pydantic import ValidationError
import logging
from utils.user_to_dict import user_db_to_dict


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/users/", response_model=ResponseModel)
def create_user(user: UserDTO, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    use_case = UserUseCase(user_repository)
    try:
        created_user = use_case.register_user(user)
    except ValidationError as ve:
        logger.error(f"ValidationError: {ve}")
        raise HTTPException(status_code=400, detail="Faltan datos obligatorios.")
    except IntegrityError as ie:
        logger.error(f"IntegrityError: {ie}")
        raise HTTPException(status_code=400, detail="Ya el usuario existe.")
    except Exception as e:
        logger.error(f"Exception: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")
    
    # Flatten the data before returning it
    flattened_data = user_db_to_dict(created_user)
    return ResponseModel(**flattened_data, message="El usuario se creó correctamente.", status_code=201)

@router.get("/users/{id}", response_model=ResponseModel)
def get_user(id: int, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_db = user_repository.find_by_id(id)
    if user_db is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Construye el objeto ResponseModel con los datos del usuario y los campos adicionales
    user = ResponseModel(**user_db.__dict__, message="Usuario encontrado", status_code=200)
    return user


