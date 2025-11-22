# models/habit.py
import uuid
from datetime import datetime
import json
import os

class Habit:
    def __init__(self, id, name, description, frequency, goal, color, active=True, created_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.frequency = frequency  # ex: "daily"
        self.goal = goal            # ex: "2 litros", "10 páginas"
        self.color = color          # ex: "#FF6B00"
        self.active = active
        self.created_at = created_at or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "frequency": self.frequency,
            "goal": self.goal,
            "color": self.color,
            "active": self.active,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class HabitModel:
    FILE_PATH = "data/habits.json"

    def __init__(self):
        self.habits = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, "r", encoding="utf-8") as f:
            return [Habit.from_dict(item) for item in json.load(f)]

    def _save(self):
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([h.to_dict() for h in self.habits], f, indent=4, ensure_ascii=False)

    def get_all(self):
        self.habits = self._load()
        return self.habits

    def get_by_id(self, habit_id):
        return next((h for h in self.habits if h.id == habit_id), None)

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
