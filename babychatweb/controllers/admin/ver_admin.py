import web
from models.usuarios import obtener_admin

render = web.template.render("views/admin", base="../master1")

class VerAdmin:
    def GET(self, uid):
        try:
            admin = obtener_admin(uid)  # Obtener el admin desde Firebase
            if not admin:
                return "Error: Administrador no encontrado."

            return render.ver_admin(admin)  # Renderiza la vista con los datos
        except Exception as e:
            print(f"Error en VerAdmin GET: {str(e)}")
            return "Error al cargar la página."
