from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService
from utils.session import set_session_user, clear_session

# login_routes = Bottle()

class LoginController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/login", method=["GET", "POST"], callback=self.login)
        self.app.route("/logout", method="GET", callback=self.logout)

    def login(self):
        if request.method == "GET":
            return self.render("loginPage")
        
        # self.user_model.users = self.user_model._load()

        username = request.forms.get("username")
        password = request.forms.get("password")

        user = self.user_service.authenticate(username, password)

        if user:
            set_session_user(user.id)
            return self.redirect("/dashboard")

        return self.render("loginPage", error="usuário ou senha incorretos.")

    def logout(self):
        clear_session()
        return self.redirect("/login")
