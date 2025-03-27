import re
import web
import json
from models.usuarios import registrar_admin

class RegistroAdmin:
    def POST(self):
        try:
            datos = web.input()
            
            # Validaciones
            if not self.validar_nombre(datos.nombres) or not self.validar_nombre(datos.primer_apellido) or not self.validar_nombre(datos.segundo_apellido):
                return json.dumps({"status": "error", "message": "Los nombres solo pueden contener letras y espacios."})
            
            if not self.validar_telefono(datos.telefono):
                return json.dumps({"status": "error", "message": "El teléfono debe contener solo números (10 dígitos)."})
            
            if not self.validar_email(datos.email):
                return json.dumps({"status": "error", "message": "Formato de correo inválido."})
            
            if datos.rango not in ["superadmin", "respuestas"]:
                return json.dumps({"status": "error", "message": "Rango inválido."})

            if not self.validar_password(datos.contrasena):
                return json.dumps({"status": "error", "message": "La contraseña debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas y números."})
            
            if datos.contrasena != datos.confirmar_contrasena:
                return json.dumps({"status": "error", "message": "Las contraseñas no coinciden."})

            # Registrar en Firebase
            resultado = registrar_admin(
                datos.nombres.strip(),
                datos.primer_apellido.strip(),
                datos.segundo_apellido.strip(),
                datos.telefono.strip(),
                datos.email.strip(),
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

    def validar_email(self, email):
        return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))

    def validar_password(self, password):
        return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$", password))
