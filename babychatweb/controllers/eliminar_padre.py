import web
from models.usuarios import eliminar_padre, obtener_padre

render = web.template.render("views/admin", base="../master1")

class EliminarPadre:
    def GET(self, uid):
        """Elimina un paciente/tutor y redirige a la lista de pacientes."""
        try:
            eliminado = eliminar_padre(uid)
            if eliminado:
                return web.seeother('/vistapacientes')  
            else:
                return "Error al eliminar el paciente."
        except Exception as e:
            return f"Error al eliminar el paciente: {str(e)}"

class ConfirmarEliminacionPadre:
    def GET(self, uid):
        """Muestra la confirmación antes de eliminar el paciente."""
        try:
            padre = obtener_padre(uid)
            if not padre:
                return "Administrador no encontrado"
            return render.confirmar_eliminacion_padre(uid, padre["nombres"])
        except Exception as e:
            return f"Error al cargar la vista de confirmación: {str(e)}"
