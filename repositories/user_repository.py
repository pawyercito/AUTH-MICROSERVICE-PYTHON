# repository.py
from sqlalchemy.orm import Session
from models.user_model_db import UserDB
from models.user_model_dto import UserDTO
from models.response_user_model import ResponseModel
from models.user_update_model import UserUpdateModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserDTO):
        db_user = UserDB(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def find_by_id(self, user_id: int) -> UserDB:
        return self.db.query(UserDB).filter(UserDB.id == user_id).first()
    
    def update_user(self, user_id: int, user_data: UserUpdateModel) -> ResponseModel:
        user = self.db.query(UserDB).filter(UserDB.id == user_id).first()
        if user is None:
            return None
        for key, value in user_data.dict().items():
            if value is not None:
                setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return ResponseModel(**user.__dict__, message="Usuario actualizado", status_code=200)
    
    