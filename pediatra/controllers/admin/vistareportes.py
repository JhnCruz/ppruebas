import web
from models.usuarios import obtener_reportes

render = web.template.render('views/admin', base="../master1")

class VistaReportes:
    def GET(self):
        try:
            reportes = obtener_reportes()  # 🔹 Obtiene las respuestas desde Firebase
            
            if reportes is None:  # 🔹 Si la consulta retorna None, asignamos una lista vacía
                reportes = []

            return render.vistareportes(reportes)  # 🔹 Pasamos siempre la lista

        except Exception as e:
            print(f"Error en VistaReportes: {str(e)}")
            return "Error al cargar la vista de reportes"
