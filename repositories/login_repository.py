# repositories/user_repository.py
from sqlalchemy.orm import Session
from models.user_model_db import UserDB

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_email(self, email: str) -> UserDB:
        return self.db.query(UserDB).filter(UserDB.correo == email).first()