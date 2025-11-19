from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.habit_controller import habit_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(habit_routes)
