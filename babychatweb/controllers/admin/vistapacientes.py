import web
from models.usuarios import obtener_pacientes

render = web.template.render('views/admin', base="../master1")

class VistaPacientes:
    def GET(self):
        try: 
            # 🔹 Obtener lista de pediatras desde el modelo
            pacientes = obtener_pacientes()
            return render.vistapacientes(pacientes)  # 🔹 Pasar la lista a la vista

        except Exception as e:
            print(f"Error en VistaPacientes: {str(e)}")
            return "Error al cargar la vista de pacientes"