import web
from models.usuarios import eliminar_pedia, obtener_pedia

render = web.template.render("views/admin", base="../master1")

class EliminarPedia:
    def GET(self, uid):
        """Elimina un Pediatra y redirige a la lista de admins."""
        try:
            eliminado = eliminar_pedia(uid)
            if eliminado:
                return web.seeother('/vistapediatras')  
            else:
                return "Error al eliminar el pediatras."
        except Exception as e:
            return f"Error al eliminar el pediatra: {str(e)}"

class ConfirmarEliminacionPedia:
    def GET(self, uid):
        """Muestra la confirmación antes de eliminar el pedia."""
        try:
            pedia = obtener_pedia(uid)
            if not pedia:
                return "Pediatra no encontrado"
            return render.confirmar_eliminacion_pedia(uid, pedia["nombres"])
        except Exception as e:
            return f"Error al cargar la vista de confirmación: {str(e)}"
