import web
from models.usuarios import obtener_admin, actualizar_admin

render = web.template.render("views/admin", base="../master1")

class EditarAdmin:
    def GET(self, uid):
        try:
            print(f"UID recibido: {uid}")  # Debug
            admin = obtener_admin(uid)
            if not admin:
                return "Error: Administrador no encontrado."
            
            print(f"Administrador obtenido: {admin}")  # Debug
            return render.editar_admin(admin)
        except Exception as e:
            print(f"Error en EditarAdmin GET: {str(e)}")
            return "Error al cargar la página."

    def POST(self, uid):
        try:
            datos = web.input()
            datos_actualizados = {
                "nombres": datos.nombres,
                "primer_apellido": datos.primer_apellido,
                "segundo_apellido": datos.segundo_apellido,
                "telefono": datos.telefono,
                "email": datos.email,
                "rango": datos.rango
            }
            
            resultado = actualizar_admin(uid, datos_actualizados)

            if resultado:
                print(f"✅ Administrador {uid} actualizado correctamente.")
                return web.seeother("/vistaadmins")
            else:
                return "Error al actualizar el administrador."
        except Exception as e:
            print(f"Error en EditarAdmin POST: {str(e)}")
            return "Error al procesar la actualización."
