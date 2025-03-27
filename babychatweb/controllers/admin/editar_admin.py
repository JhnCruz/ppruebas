import web
from models.usuarios import obtener_admin, actualizar_admin

render = web.template.render("views/admin", base="../master1")

class EditarAdmin:
    def GET(self, uid):
        try:
            admin = obtener_admin(uid)
            if not admin:
                return "Error: Administrador no encontrado."
            return render.editar_admin(admin)
        except Exception as e:
            print(f"Error en EditarAdmin GET: {str(e)}")
            return "Error al cargar la página de edición."

    def POST(self, uid):
        try:
            form = web.input()
            datos_actualizados = {
                "nombre": form.nombre,
                "apellido1": form.apellido1,
                "apellido2": form.apellido2,
                "telefono": form.telefono,
                "correo": form.correo,
                "rango": form.rango
            }

            if actualizar_admin(uid, datos_actualizados):
                raise web.seeother("/vistaadmins")
            else:
                return "Error al actualizar el administrador."
        except Exception as e:
            print(f"Error en EditarAdmin POST: {str(e)}")
            return "Error al procesar la actualización."
