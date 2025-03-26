import web
from controllers.indexadmin import IndexAdmin
from controllers.admin.vistaadmins import VistaAdmins
from controllers.admin.vistapediatras import VistaPediatras
from controllers.admin.vistapacientes import VistaPacientes
from controllers.admin.vistarespuestas import VistaRespuestas
from controllers.admin.vistareportes import VistaReportes
from controllers.admin.registroadmin import RegistroAdmin

web.config.debug = False  

# Definir rutas
urls = (
    '/', 'IndexAdmin',
    '/registro_admin', 'RegistroAdmin',
    '/vistaadmins', 'VistaAdmins',
    '/vistapediatras', 'VistaPediatras',
    '/vistapacientes', 'VistaPacientes',
    '/vistarespuestas', 'VistaRespuestas',
    '/vistareportes', 'VistaReportes'
)

app = web.application(urls, globals())

# 📌 Asegurar que la sesión esté configurada correctamente
if web.config.get('_session') is None:  # Evitar que la sesión se reinicialice en cada request
    session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"usuario": None})
    web.config._session = session  # Guardar la sesión en web.config

# 📌 Hacer que session sea accesible globalmente
def session_hook():
    web.ctx.session = web.config._session

app.add_processor(web.loadhook(session_hook))

if __name__ == "__main__":
    app.run()
