import json
import os
from datetime import datetime, date


class HabitLog:
    def __init__(self, id, habit_id, user_id, log_date, done):
        self.id = id
        self.habit_id = habit_id
        self.user_id = user_id
        self.log_date = log_date
        self.done = done

    def to_dict(self):
        return {
            "id": self.id,
            "habit_id": self.habit_id,
            "user_id": self.user_id,
            "log_date": self.log_date,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class HabitLogModel:
    FILE_PATH = "./data/habits_log.json"

    def __init__(self):
        self.logs = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, "r", encoding="utf-8") as f:
            return [HabitLog.from_dict(l) for l in json.load(f)]

    def _save(self):
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([l.to_dict() for l in self.logs], f, indent=4, ensure_ascii=False)

    def add(self, log):
        self.logs.append(log)
        self._save()

    def get_today_by_habit(self, habit_id, user_id):
        self.logs = self._load()
        today = date.today().isoformat()
        return next(
            (l for l in self.logs
             if l.habit_id == habit_id and l.user_id == user_id and l.log_date == today),
            None
        )

    def get_by_user(self, user_id):
        self.logs = self._load()
        return [l for l in self.logs if l.user_id == user_id]
    
    def delete_by_habit(self, habit_id):
        self.logs = [l for l in self.logs if l.habit_id != habit_id]
        self._save()
