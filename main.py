from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware
from controllers.user_register_controller import router as user_router
from controllers.login_controller import router as login_router
from controllers.update_patient_information_controller import router as update_patient_information_router
from db.database import engine, Base

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Ajusta esto a la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas de los controladores
app.include_router(user_router)
app.include_router(login_router)
app.include_router(update_patient_information_router)

@app.get("/")
def read_root():
    return {"message": "IM ALIVE!"}

@app.on_event("startup")
async def startup():
    print("Starting up...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
