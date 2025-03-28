import re
import web
from models.usuarios import registrar_pediatra

render = web.template.render("views/")

class Registro:
    def GET(self):
        return render.registro()  
    
    def POST(self):
        try:
            datos = web.input()

            if not self.validar_nombre(datos.nombres) or not self.validar_nombre(datos.primer_apellido) or not self.validar_nombre(datos.segundo_apellido):
                return "Error: El nombre y apellidos solo pueden contener letras y espacios."
            
            if not self.validar_email(datos.email):
                return "Error: Formato de correo inválido."
            
            if not self.validar_nacimiento(datos.nacimiento):
                return "Error: La fecha de nacimiento debe ser en formato YYYY-MM-DD."
            
            if not self.validar_licencia(datos.licencia):
                return "Error: La licencia debe ser un número válido."
            
            if not self.validar_password(datos.password):
                return "Error: La contraseña debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas y números."
            
            if datos.password != datos.password_confirm:
                return "Error: Las contraseñas no coinciden."
            
            # Llamar al modelo para registrar al usuario con rol "user"
            resultado = registrar_pediatra(
                datos.nombres.strip(),
                datos.primer_apellido.strip(),
                datos.segundo_apellido.strip(),
                datos.nacimiento.strip(),
                datos.email.strip(),
                datos.licencia.strip(),
                datos.password.strip()
            )
            
            if resultado:
                raise web.seeother('/iniciosesion')  
            else:
                return "Error: No se pudo registrar el usuario. Es posible que el correo ya esté en uso."
                
        except Exception as e:
            return f"Error inesperado: {str(e)}"

    def validar_nombre(self, texto):
        """Permite solo letras y espacios en nombres y apellidos"""
        return bool(re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", texto))
    
    def validar_email(self, email):
        """Verifica que el correo tenga un formato válido"""
        return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))
    
    def validar_nacimiento(self, fecha):
        """Verifica que la fecha esté en formato YYYY-MM-DD"""
        return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", fecha))
    
    def validar_licencia(self, licencia):
        """La licencia debe ser un número válido"""
        return licencia.isdigit()
    
    def validar_password(self, password):
        """Verifica que la contraseña tenga al menos 8 caracteres, una mayúscula, una minúscula y un número"""
        return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$", password))