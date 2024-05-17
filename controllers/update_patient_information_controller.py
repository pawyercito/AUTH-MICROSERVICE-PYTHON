# controllers/user_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.response_user_model import ResponseModel
from repositories.user_repository import UserRepository
from models.user_update_model import UserUpdateModel
from db.database import get_db

router = APIRouter()

@router.put("/users/{id}", response_model=ResponseModel)
def update_user(id: int, user_data: UserUpdateModel, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user = user_repository.update_user(id, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user