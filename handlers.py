# handler.py
from fastapi import FastAPI
from controllers.user_register_controller import router as user_router
from db.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from controllers.login_controller import router as login_router
from controllers.update_patient_information_controller import router as update_patient_information_router

app = FastAPI()

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(user_router)
app.include_router(login_router)
app.include_router(update_patient_information_router)

