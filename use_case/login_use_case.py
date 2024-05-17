# use_case/login_use_case.py
from models.user_model_db import UserDB
from repositories.login_repository import UserRepository
from models.user_model_dto import UserDTO

class LoginUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login_user(self, login_dto: UserDTO) -> UserDB:
        user = self.user_repository.find_by_email(login_dto.correo)
        if user and user.check_password(login_dto.contraseña):
            return user
        else:
            raise ValueError("Correo o contraseña incorrectos.")