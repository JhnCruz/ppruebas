import pyrebase
import bcrypt
import json

config = {
    "apiKey": "AIzaSyAyRBgtd5Ayvus1La1gL0DcISCR0xTNWXA",
    "authDomain": "pruebas-a7640.firebaseapp.com",
    "databaseURL": "https://pruebas-a7640-default-rtdb.firebaseio.com",
    "storageBucket": "pruebas-a7640.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()

def registrar_admin(nombre, apellido1, apellido2, telefono, correo, rango, password):
    try:
        user = auth.create_user_with_email_and_password(correo, password)  

        datos_admin = {
            "nombre": nombre,
            "apellido1": apellido1,
            "apellido2": apellido2,
            "telefono": telefono,
            "correo": correo,
            "rango": rango,
            "uid": user["localId"],
            "rol": "admin"
        }

        db.child("usuarios").child(user["localId"]).set(datos_admin)

        print("Administrador registrado correctamente.")
        return True
    except Exception as e:
        print(f"Error al registrar administrador: {str(e)}")
        return False

def obtener_administradores():
    try:
        # 🔹 Obtener todos los usuarios desde Firebase
        usuarios = db.child("usuarios").get().val()

        if not usuarios:
            return []  # 🔹 Si no hay usuarios, retorna una lista vacía

        # 🔹 Filtrar solo los usuarios con rol "admin"
        administradores = [
            {"uid": uid, **datos} for uid, datos in usuarios.items() if datos.get("rol") == "admin"
        ]
        return administradores

    except Exception as e:
        print(f"Error al obtener administradores: {str(e)}")
        return []

def obtener_pediatras():
    try:
        # Obtener Todos los usuarios desde FIrebase
        usuarios = db.child("usuarios").get().val()

        if not usuarios:
            return []  # 🔹 Si no hay usuarios, retorna una lista vacía
        # Filtrar solo los usuarios con el rol "pedia"
        pediatras = [
            {"uid": uid, **datos} for uid, datos in usuarios.items() if datos.get("rol") == "pedia"
        ]
        return pediatras

    except Exception as e:
        print(f"Error al obtener pediatras: {str(e)}")
        return []

def obtener_respuestas():
    try:
        respuestas = db.child("respuestas").get().val()

        if not respuestas:
            return []

        # Convertir el diccionario en una lista de respuestas
        lista_respuestas = [
            {
                "uid": uid,
                "error": datos.get("error", ""),
                "pregunta": datos.get("pregunta", ""),
                "respuesta": datos.get("respuesta", "")
            }
            for uid, datos in respuestas.items()
        ]

        return lista_respuestas

    except Exception as e:
        print(f"Error al obtener respuestas: {str(e)}")
        return []

def obtener_reportes():
    try:
        reportes = db.child("reportes").get().val()

        if not reportes:
            return []

        # Convertir el diccionario en una lista de respuestas
        lista_reportes = [
            {
                "uid": uid,
                "error": datos.get("error", ""),
                "fecha": datos.get("fecha", ""),
                "nombre_usuario": datos.get("nombre_usuario", "")
            }
            for uid, datos in reportes.items()
        ]

        return lista_reportes

    except Exception as e:
        print(f"Error al obtener reportes: {str(e)}")
        return []
