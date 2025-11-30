from bottle import Bottle, request
from .base_controller import BaseController
from services.habit_service import HabitService
from services.habit_log_service import HabitLogService
from utils.session import get_session_user

class HabitController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.habit_service = HabitService()
        self.habit_log_service = HabitLogService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/habits', method='GET', callback=self.list_habits)
        self.app.route('/habits/add', method=['GET', 'POST'], callback=self.add_habit)
        self.app.route('/habits/edit/<habit_id:int>', method=['GET', 'POST'], callback=self.edit_habit)
        self.app.route('/habits/delete/<habit_id:int>', method='POST', callback=self.delete_habit)

    def list_habits(self):
        user_id = get_session_user()
        if not user_id:
            return self.redirect("/login")

        user_id = int(user_id)

        habits = self.habit_service.get_by_user(user_id)
        today_logs = self.habit_log_service.get_today_user_logs(user_id)
        done_ids = {log.habit_id for log in today_logs}

        habits_with_status = []
        for h in habits:
            habits_with_status.append({
                "id": h.id,
                "name": h.name,
                "description": h.description,
                "frequency": h.frequency,
                "done": h.id in done_ids 
            })

        return self.render(
            "habits",
            habits=habits_with_status
        )

    def add_habit(self):
        if request.method == 'GET':
            return self.render('habits_form', habit=None, action='/habits/add')
        else:
            self.habit_service.save()
            self.redirect('/dashboard')

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
