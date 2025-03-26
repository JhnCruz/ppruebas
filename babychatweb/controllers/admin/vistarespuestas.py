import web
from models.usuarios import obtener_respuestas

render = web.template.render('views/admin', base="../master1")

class VistaRespuestas:
    def GET(self):
        try:
            respuestas = obtener_respuestas()  # 🔹 Obtiene las respuestas desde Firebase
            
            if respuestas is None:  # 🔹 Si la consulta retorna None, asignamos una lista vacía
                respuestas = []

            return render.vistarespuestas(respuestas)  # 🔹 Pasamos siempre la lista

        except Exception as e:
            print(f"Error en VistaRespuestas: {str(e)}")
            return "Error al cargar la vista de respuestas"
