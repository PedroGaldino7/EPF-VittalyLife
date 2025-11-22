from bottle import request
from .base_controller import BaseController
from services.user_service import UserService

class RegisterController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/register", method=["GET", "POST"], callback=self.register)

    def register(self):
        # Se só está abrindo
        if request.method == "GET":
            return self.render("cadPage")

        # Se os dados foram enviados
        username = request.forms.get("username")
        email = request.forms.get("email")
        password = request.forms.get("password")

        # Salva usando o service já existente
        self.user_service.create_user(username, email, password)

        # Depois de cadastrar, vai para o login
        return self.redirect("/login")
