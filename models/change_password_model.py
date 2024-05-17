# models/user_model.py
from pydantic import BaseModel

class ChangePasswordModel(BaseModel):
    token: str
    new_password: str