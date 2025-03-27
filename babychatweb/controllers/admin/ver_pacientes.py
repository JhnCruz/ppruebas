import web
from models.usuarios import obtener_padre

render = web.template.render("views/admin", base="../master1")

class VerPacientes:
    def GET(self, uid):
        try:
            padre = obtener_padre(uid)  # Obtener el admin desde Firebase
            if not padre:
                return "Error: Paciente no encontrado."

            return render.ver_pacientes(padre)  # Renderiza la vista con los datos
        except Exception as e:
            print(f"Error en VerPaciente GET: {str(e)}")
            return "Error al cargar la página."
