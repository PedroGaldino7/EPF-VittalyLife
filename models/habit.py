from datetime import datetime
from models.base_model import BaseJsonModel

class Habit:
    def __init__(self, id, user_id, name, description, frequency, active=True, created_at=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.frequency = frequency
        self.created_at = created_at or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "frequency": self.frequency,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class HabitModel(BaseJsonModel):
    file_path = "./data/habits.json"

    def __init__(self):
        raw_data = self._load_data()
        self.habits = [Habit.from_dict(item) for item in raw_data]

    def _save(self):
        self._save_data([h.to_dict() for h in self.habits])

    def get_all(self):
        raw_data = self._load_data()
        self.habits = [Habit.from_dict(item) for item in raw_data]
        return self.habits

    def get_by_id(self, habit_id):
        self.get_all()
        return next((h for h in self.habits if h.id == habit_id), None)
    
    def get_by_user(self, user_id):
        self.get_all()
        return [h for h in self.habits if h.user_id == user_id]

    def add(self, habit):
        self.habits.append(habit)
        self._save()

    def update(self, updated_habit):
        for i, h in enumerate(self.habits):
            if h.id == updated_habit.id:
                self.habits[i] = updated_habit
                self._save()
                break

    def delete(self, habit_id):
        self.habits = [h for h in self.habits if h.id != habit_id]
        self._save()

    def delete_by_user(self, user_id):
        self.habits = [h for h in self.habits if h.user_id != user_id]
        self._save()