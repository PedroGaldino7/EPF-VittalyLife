from bottle import static_file
from utils.session import get_session_user
from services.user_service import UserService

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()


    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.homePage)
        self.app.route('/loginPage', method='GET', callback=self.login_page)
        self.app.route('/cadPage', method='GET', callback=self.cad_page)
        self.app.route('/helper', method=['GET'], callback=self.helper)

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)


    def homePage(self):
        return self.render('homePage')
    
    def login_page(self):
        return self.render('loginPage')
    
    def cad_page(self):
        return self.render('cadPage')

    def helper(self):
        return self.render('helper-final')
    
    def get_logged_user(self):
        user_id = get_session_user()
        if not user_id:
            return None
        
        return UserService().get_by_id(int(user_id))

    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template, **context):
        """Método auxiliar para renderizar templates"""
        from bottle import template as render_template
        return render_template(template, **context)


    def redirect(self, path, code=302):
        """Redirecionamento robusto com tratamento de erros"""
        from bottle import HTTPResponse, response as bottle_response

        try:
            bottle_response.status = code
            bottle_response.set_header('Location', path)
            return bottle_response
        except Exception as e:
            print(f"ERRO NO REDIRECT: {type(e).__name__} - {str(e)}")
            return HTTPResponse(
                body=f'<script>window.location.href="{path}";</script>',
                status=200,
                headers={'Content-Type': 'text/html'}
            )
