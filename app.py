from bottle import Bottle, template
from config import Config
from bottle import run

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.setup_errors()

    def setup_errors(self):
        @self.bottle.error(404)
        def error404(error):
            return template('error', error=error)

        @self.bottle.error(500)
        def error500(error):
            return template('error', error=error)

    def setup_routes(self):
        from controllers import init_controllers

        print('Inicializa rotas!')
        init_controllers(self.bottle)

    def run(self):
        self.setup_routes()

        run(
            app=self.bottle,
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()
