from controllers.user_controller import UserController
from controllers.habit_controller import HabitController
from controllers.login_controller import LoginController
from controllers.dashboard_controller import DashboardController
from controllers.register_controller import RegisterController


def init_controllers(app):
    UserController(app)
    HabitController(app)
    LoginController(app)
    DashboardController(app)
    RegisterController(app)
