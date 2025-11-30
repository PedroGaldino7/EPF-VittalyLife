from datetime import date
from models.base_model import BaseJsonModel

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


class HabitLogModel(BaseJsonModel):
    file_path = "./data/habits_log.json"

    def __init__(self):
        raw_data = self._load_data()
        self.logs = [HabitLog.from_dict(l) for l in raw_data]

    def _save(self):
        self._save_data([l.to_dict() for l in self.logs])

    def add(self, log):
        self.logs.append(log)
        self._save()

    def get_today_by_habit(self, habit_id, user_id):
        raw_data = self._load_data()
        self.logs = [HabitLog.from_dict(l) for l in raw_data]
        
        today = date.today().isoformat()
        return next(
            (l for l in self.logs
             if l.habit_id == habit_id and l.user_id == user_id and l.log_date == today),
            None
        )

    def get_by_user(self, user_id):
        raw_data = self._load_data()
        self.logs = [HabitLog.from_dict(l) for l in raw_data]
        return [l for l in self.logs if l.user_id == user_id]
    
    def delete_by_habit(self, habit_id):
        self.logs = [l for l in self.logs if l.habit_id != habit_id]
        self._save()
    
    def get_today_user_logs(self, user_id):

        raw_data = self._load_data()
        self.logs = [HabitLog.from_dict(l) for l in raw_data]
        today = date.today().isoformat()
        return [
            l for l in self.logs
            if l.user_id == user_id and l.log_date == today
        ]