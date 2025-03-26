import web

render = web.template.render('views/')

class IndexAdmin:
    def GET(self):
        try: 
            return render.indexadmin() 
        except Exception as error:
            message = {
                "error": error.args[0] }
            print(f"ERROR: {message}")
            return message