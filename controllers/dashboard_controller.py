from bottle import Bottle
from .base_controller import BaseController
from services.user_service import UserService
from utils.session import get_session_user
from services.habit_service import HabitService
from services.habit_log_service import HabitLogService

dashboard_routes = Bottle()

class DashboardController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.habit_service = HabitService()
        self.log_service = HabitLogService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/dashboard", method="GET", callback=self.index)

    def index(self):
        user_id = get_session_user()
        if not user_id:
            return self.redirect("/login")

        user_id = int(user_id)

        habits = self.habit_service.get_by_user(user_id)
        today_logs = self.log_service.get_today_user_logs(user_id)
        done_ids = {log.habit_id for log in today_logs}

        pending = [h for h in habits if h.id not in done_ids]

        total = len(habits)
        concluidos = len(done_ids)
        
        if total > 0:
            porcentagem = int((concluidos / total) * 100)
        else:
            porcentagem = 0

        return self.render(
            "dashboard",
            user=self.get_user(user_id),
            pending_habits=pending,
            porcentagem=porcentagem
        )