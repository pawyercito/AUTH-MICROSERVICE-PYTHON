# use_case.py
import hashlib
from repositories.user_repository import UserRepository
from models.user_model_dto import UserDTO

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, user: UserDTO):
        hashed_password = hashlib.sha256(user.contraseña.encode()).hexdigest()
        user.contraseña = hashed_password  # La contraseña se hashea antes de pasar al repositorio
        return self.user_repository.create_user(user)