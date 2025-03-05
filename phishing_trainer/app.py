import web
from controllers.phishing_controller import PhishingController

# Definir rutas del proyecto en web.py
urls = (
    "/", "Index",
    "/info", "Info",
    "/examples", "Examples",
    "/generate_question", "GenerateQuestion"
)

# Controladores de cada ruta
class Index:
    def GET(self):
        return web.template.frender("templates/index.html")()

class Info:
    def GET(self):
        controller = PhishingController()
        return web.template.frender("templates/info.html")(controller.GET_info())

class Examples:
    def GET(self):
        controller = PhishingController()
        return web.template.frender("templates/info.html")(controller.GET_examples())

class GenerateQuestion:
    def GET(self):
        controller = PhishingController()
        return controller.GET_generate_question()

# Ejecutar la aplicación web.py
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
