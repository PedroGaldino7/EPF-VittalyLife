from bottle import Bottle
from .base_controller import BaseController
from services.user_service import UserService
from utils.session import get_session_user

dashboard_routes = Bottle()

class DashboardController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/dashboard", method="GET", callback=self.index)

    def index(self):
        user_id = get_session_user()

        if not user_id:
            return self.redirect("/login")

        user = self.user_service.get_by_id(int(user_id))
        return self.render("dashboard", user=user)
