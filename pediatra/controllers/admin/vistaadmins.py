import web
from models.usuarios import obtener_administradores

render = web.template.render('views/admin', base="../master1")

class VistaAdmins:
    def GET(self):
        try:
            # 🔹 Obtener lista de administradores desde el modelo
            administradores = obtener_administradores()
            return render.vistaadmins(administradores)  # 🔹 Pasar la lista a la vista

        except Exception as e:
            print(f"Error en VistaAdmins: {str(e)}")
            return "Error al cargar la vista de administradores"


