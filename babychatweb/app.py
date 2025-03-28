import web
from controllers.index import Index
from controllers.registro import Registro
from controllers.iniciosesion import Iniciosesion
from controllers.indexadmin import IndexAdmin
from controllers.admin.vistaadmins import VistaAdmins
from controllers.admin.vistapediatras import VistaPediatras
from controllers.admin.vistapacientes import VistaPacientes
from controllers.admin.vistarespuestas import VistaRespuestas
from controllers.admin.vistareportes import VistaReportes
from controllers.admin.registroadmin import RegistroAdmin
from controllers.eliminar_admin import EliminarAdmin, ConfirmarEliminacion
from controllers.eliminar_pedia import EliminarPedia, ConfirmarEliminacionPedia
from controllers.eliminar_padre import EliminarPadre, ConfirmarEliminacionPadre
from controllers.admin.ver_admin import VerAdmin
from controllers.admin.ver_pediatra import VerPedia
from controllers.admin.ver_pacientes import VerPacientes
from controllers.admin.editar_admin import EditarAdmin

web.config.debug = False  

urls = (
    '/', 'Index',
    '/indexadmin', 'IndexAdmin',
    '/registro', 'Registro',
    '/iniciosesion', 'Iniciosesion',
    '/registro_admin', 'RegistroAdmin',
    '/vistaadmins', 'VistaAdmins',
    '/vistapediatras', 'VistaPediatras',
    '/vistapacientes', 'VistaPacientes',
    '/vistarespuestas', 'VistaRespuestas',
    "/eliminar_admin/(.*)", "EliminarAdmin",
    "/confirmar_eliminacion/(.*)", "ConfirmarEliminacion",
    "/eliminar_pedia/(.*)", "EliminarPedia",
    "/confirmar_eliminacion_pedia/(.*)", "ConfirmarEliminacionPedia",
    "/eliminar_padre/(.*)", "EliminarPadre",
    "/confirmar_eliminacion_padre/(.*)", "ConfirmarEliminacionPadre",
    "/ver_admin/(.*)", "VerAdmin",
    "/ver_pedia/(.*)", "VerPedia",
    "/ver_pacientes/(.*)", "VerPacientes",
    '/vistareportes', 'VistaReportes',
    "/editar_admin/(.*)", "EditarAdmin"
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
