from models.user_model_db import UserDB

def user_db_to_dict(user_db: UserDB):
    return {
        "id": user_db.id,
        "nombre": user_db.nombre,
        "apellido": user_db.apellido,
        "correo": user_db.correo,
        "numero_telefonico": user_db.numero_telefonico,
        "contraseña": user_db.contraseña,
        "sexo": user_db.sexo,
        "edad": user_db.edad,
        "peso": user_db.peso,
        "estatura": user_db.estatura,
        "cedula_identidad": user_db.cedula_identidad,
        "direccion": user_db.direccion,
        "fecha_nacimiento": user_db.fecha_nacimiento,
        "tipo_sangre": user_db.tipo_sangre,
    }