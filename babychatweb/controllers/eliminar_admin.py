import web
from models.usuarios import eliminar_admin, obtener_admin

render = web.template.render("views/admin", base="../master1")

class EliminarAdmin:
    def GET(self, uid):
        """Elimina un administrador y redirige a la lista de admins."""
        try:
            eliminado = eliminar_admin(uid)
            if eliminado:
                return web.seeother('/vistaadmins')  
            else:
                return "Error al eliminar el administrador."
        except Exception as e:
            return f"Error al eliminar el administrador: {str(e)}"

class ConfirmarEliminacion:
    def GET(self, uid):
        """Muestra la confirmación antes de eliminar el admin."""
        try:
            admin = obtener_admin(uid)
            if not admin:
                return "Administrador no encontrado"
            return render.confirmar_eliminacion(uid, admin["nombres"])
        except Exception as e:
            return f"Error al cargar la vista de confirmación: {str(e)}"
