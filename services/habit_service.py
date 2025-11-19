# services/habit_service.py
from bottle import request
from models.habit import HabitModel, Habit

class HabitService:
    def __init__(self):
        self.habit_model = HabitModel()

    def get_all(self):
        return self.habit_model.get_all()

    def get_by_id(self, habit_id):
        return self.habit_model.get_by_id(habit_id)

    def save(self):
        habits = self.habit_model.get_all()
        last_id = max([h.id for h in habits], default=0)
        new_id = last_id + 1

        name = request.forms.get("name")
        description = request.forms.get("description")
        frequency = request.forms.get("frequency")
        goal = request.forms.get("goal")
        color = request.forms.get("color")
        active = request.forms.get("active") == "on"

        habit = Habit(
            id=new_id,
            name=name,
            description=description,
            frequency=frequency,
            goal=goal,
            color=color,
            active=active
        )

        self.habit_model.add(habit)

    def edit(self, habit):
        habit.name = request.forms.get("name")
        habit.description = request.forms.get("description")
        habit.frequency = request.forms.get("frequency")
        habit.goal = request.forms.get("goal")
        habit.color = request.forms.get("color")
        habit.active = request.forms.get("active") == "on"

        self.habit_model.update(habit)

    def delete(self, habit_id):
        self.habit_model.delete(habit_id)
