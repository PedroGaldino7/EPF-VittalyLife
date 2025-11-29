from bottle import request, Bottle
from .base_controller import BaseController
from services.habit_log_service import HabitLogService
from utils.session import get_session_user

class HabitLogController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = HabitLogService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/habits/checkin/<habit_id:int>", method="POST", callback=self.checkin)

    def checkin(self, habit_id):
        user_id = get_session_user()

        if not user_id:
            return self.redirect("/login")

        self.service.check_in(habit_id, int(user_id))

        return self.redirect("/dashboard")

habit_log_routes = Bottle()