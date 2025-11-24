# controllers/habit_controller.py
from bottle import Bottle, request
from .base_controller import BaseController
from services.habit_service import HabitService
from utils.session import get_session_user

class HabitController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.habit_service = HabitService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/habits', method='GET', callback=self.list_habits)
        self.app.route('/habits/add', method=['GET', 'POST'], callback=self.add_habit)
        self.app.route('/habits/edit/<habit_id:int>', method=['GET', 'POST'], callback=self.edit_habit)
        self.app.route('/habits/delete/<habit_id:int>', method='POST', callback=self.delete_habit)

    def list_habits(self):
        user_id = get_session_user()
        habits = self.habit_service.get_by_user(user_id)
        return self.render("habits", habits=habits)

    def add_habit(self):
        if request.method == 'GET':
            return self.render('habits_form', habit=None, action='/habits/add')
        else:
            self.habit_service.save()
            self.redirect('/habits')

    def edit_habit(self, habit_id):
        habit = self.habit_service.get_by_id(habit_id)
        if request.method == 'GET':
            return self.render('habits_form', habit=habit, action=f'/habits/edit/{habit_id}')
        else:
            self.habit_service.edit(habit)
            self.redirect('/habits')

    def delete_habit(self, habit_id):
        self.habit_service.delete(habit_id)
        self.redirect('/habits')


habit_routes = Bottle()
habit_controller = HabitController(habit_routes)
