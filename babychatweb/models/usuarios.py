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

def registrar_pediatra(nombres, primer_apellido, segundo_apellido, nacimiento, email, licencia, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)  

        datos_usuario = {
            "nombres": nombres,
            "primer_apellido": primer_apellido,
            "segundo_apellido": segundo_apellido,
            "nacimiento": nacimiento,
            "email": email,
            "licencia": licencia,
            "uid": user["localId"],
            "rol": "pedia"
        }

        # Guardar en Firebase
        db.child("usuarios").child(user["localId"]).set(datos_usuario)

        print("Usuario registrado correctamente.")
        return True

    except Exception as e:
        print(f"Error al registrar usuario: {str(e)}")
        return False

def registrar_admin(nombres, primer_apellido, segundo_apellido, telefono, email, rango, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)  

        datos_admin = {
            "nombres": nombres,
            "primer_apellido": primer_apellido,
            "segundo_apellido": segundo_apellido,
            "telefono": telefono,
            "email": email,
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

def iniciar_sesion(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        uid = user["localId"]
        
        datos_usuario = db.child("usuarios").child(email.replace(".", ",")).get().val()
        
        if datos_usuario:
            print("Inicio de sesión exitoso.")
            return datos_usuario  
        else:
            print("No se encontraron datos del usuario.")
            return None

    except Exception as e:
        print(f"Error en el inicio de sesión: {str(e)}")
        return None

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

def obtener_pacientes():
    try:
        # 🔹 Obtener todos los usuarios desde Firebase
        usuarios = db.child("usuarios").get().val()

        if not usuarios:
            return []  # 🔹 Si no hay usuarios, retorna una lista vacía

        # 🔹 Filtrar solo los usuarios con rol "admin"
        pacientes = [
            {"uid": uid, **datos} for uid, datos in usuarios.items() if datos.get("rol") == "padre"
        ]
        return pacientes

    except Exception as e:
        print(f"Error al obtener pacientes: {str(e)}")
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
                "calidadrespuesta": datos.get("calidadrespuesta", ""),
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

def obtener_admin(uid):
    """Obtiene la información de un administrador por UID."""
    try:
        admin = db.child("usuarios").child(uid).get().val()
        return admin if admin else None
    except Exception as e:
        print(f"Error al obtener admin: {str(e)}")
        return None

def eliminar_admin(uid):
    """Elimina un administrador por su UID en Firebase."""
    try:
        db.child("usuarios").child(uid).remove()  
        return True
    except Exception as e:
        print(f"Error al eliminar usuario: {str(e)}")
        return False

def obtener_pedia(uid):
    """Obtiene la información de un pediatra por UID."""
    try:
        pedia = db.child("usuarios").child(uid).get().val()
        return pedia if pedia else None
    except Exception as e:
        print(f"Error al obtener admin: {str(e)}")
        return None

def eliminar_pedia(uid):
    """Elimina un pediatra por su UID en Firebase."""
    try:
        db.child("usuarios").child(uid).remove()  
        return True
    except Exception as e:
        print(f"Error al eliminar pediatra: {str(e)}")
        return False

def obtener_padre(uid):
    """Obtiene la información de un pediatra por UID."""
    try:
        padre = db.child("usuarios").child(uid).get().val()
        return padre if padre else None
    except Exception as e:
        print(f"Error al obtener padre: {str(e)}")
        return None

def eliminar_padre(uid):
    """Elimina un padre por su UID en Firebase."""
    try:
        db.child("usuarios").child(uid).remove()  
        return True
    except Exception as e:
        print(f"Error al eliminar pediatra: {str(e)}")
        return False

def actualizar_admin(uid, datos_actualizados):
    """Actualiza los datos de un administrador en Firebase."""
    try:
        db.child("usuarios").child(uid).update(datos_actualizados)
        return True
    except Exception as e:
        print(f"Error al actualizar administrador: {str(e)}")
        return False

