import web

urls = [
    '/','mvc.controllers.alumnos.index.Index', 
    '/index/?','mvc.controllers.alumnos.index.Index',
    '/insertar/?','mvc.controllers.alumnos.insertar.Insertar',
    '/borrar/(.*)','mvc.controllers.alumnos.borrar.Borrar', # /(.&) NOS PERMITE OBTENER PARAMETROS
    '/view/(.*)','mvc.controllers.alumnos.view.View',
    '/modificar/(.*)','mvc.controllers.alumnos.modificar.Modificar',
    '/list/?','mvc.controllers.alumnos.list.List',
    '/profile/?','mvc.controllers.alumnos.profile.Profile',
    '/estudioEco/?','mvc.controllers.alumnos.estudioEco.EstudioEco',
    '/planta/?','mvc.controllers.alumnos.planta.Planta',
    '/reciclar/?','mvc.controllers.alumnos.reciclar.Reciclar',
    '/proteccionAmbiental/?','mvc.controllers.alumnos.proteccionAmbiental.ProteccionAmbiental',
    '/basura/?','mvc.controllers.alumnos.basura.Basura',
    '/agua/?','mvc.controllers.alumnos.agua.Agua',
    '/iniciosesion/?','mvc.controllers.alumnos.iniciosesion.InicioSesion',
    '/registro/?','mvc.controllers.alumnos.registro.Registro',


] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()