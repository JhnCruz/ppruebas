import web
from models.usuarios import obtener_pediatras

render = web.template.render('views/admin', base="../master1")

class VistaPediatras:
    def GET(self):
        try: 
            # 🔹 Obtener lista de pediatras desde el modelo
            pediatras = obtener_pediatras()
            return render.vistapediatras(pediatras)  # 🔹 Pasar la lista a la vista

        except Exception as e:
            print(f"Error en VistaPediatras: {str(e)}")
            return "Error al cargar la vista de pediatras"