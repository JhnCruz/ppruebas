import re
import web
import json
from models.usuarios import registrar_admin

class RegistroAdmin:
    def POST(self):
        try:
            datos = web.input()
            
            # Validaciones
            if not self.validar_nombre(datos.nombre) or not self.validar_nombre(datos.apellido1) or not self.validar_nombre(datos.apellido2):
                return json.dumps({"status": "error", "message": "Los nombres solo pueden contener letras y espacios."})
            
            if not self.validar_telefono(datos.telefono):
                return json.dumps({"status": "error", "message": "El teléfono debe contener solo números (10 dígitos)."})
            
            if not self.validar_correo(datos.correo):
                return json.dumps({"status": "error", "message": "Formato de correo inválido."})
            
            if datos.rango not in ["superadmin", "respuestas"]:
                return json.dumps({"status": "error", "message": "Rango inválido."})

            if not self.validar_password(datos.contrasena):
                return json.dumps({"status": "error", "message": "La contraseña debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas y números."})
            
            if datos.contrasena != datos.confirmar_contrasena:
                return json.dumps({"status": "error", "message": "Las contraseñas no coinciden."})

            # Registrar en Firebase
            resultado = registrar_admin(
                datos.nombre.strip(),
                datos.apellido1.strip(),
                datos.apellido2.strip(),
                datos.telefono.strip(),
                datos.correo.strip(),
                datos.rango.strip(),
                datos.contrasena.strip()
            )
            
            if resultado:
                return json.dumps({"status": "success", "message": "Administrador registrado con éxito."})
            else:
                return json.dumps({"status": "error", "message": "No se pudo registrar al administrador."})
                
        except Exception as e:
            return json.dumps({"status": "error", "message": f"Error inesperado: {str(e)}"})

    def validar_nombre(self, texto):
        return bool(re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", texto))

    def validar_telefono(self, telefono):
        return bool(re.match(r"^\d{10}$", telefono))  # 10 dígitos

    def validar_correo(self, correo):
        return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo))

    def validar_password(self, password):
        return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$", password))
