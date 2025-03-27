import web
from models.usuarios import obtener_pedia

render = web.template.render("views/admin", base="../master1")

class VerPedia:
    def GET(self, uid):
        try:
            pedia = obtener_pedia(uid)  # Obtener el admin desde Firebase
            if not pedia:
                return "Error: Pediatra no encontrado."

            return render.ver_pedia(pedia)  # Renderiza la vista con los datos
        except Exception as e:
            print(f"Error en VerPedia GET: {str(e)}")
            return "Error al cargar la página."
