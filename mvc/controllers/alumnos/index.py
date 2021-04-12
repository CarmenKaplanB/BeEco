import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/alumnos/")

class Index():
    
    def GET(self):
        try:
            return render.index() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.
