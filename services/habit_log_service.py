from datetime import date
from models.habit_log import HabitLogModel, HabitLog


class HabitLogService:
    def __init__(self):
        self.model = HabitLogModel()

    def check_in(self, habit_id, user_id):
        today = date.today().isoformat()

        # Se já marcou hoje, retorna
        existing = self.model.get_today_by_habit(habit_id, user_id)
        if existing:
            return existing

        # Gerar novo ID
        new_id = max([l.id for l in self.model.logs], default=0) + 1

        log = HabitLog(
            id=new_id,
            habit_id=habit_id,
            user_id=user_id,
            log_date=today,
            done=True
        )

        self.model.add(log)
        return log

    def get_today_user_logs(self, user_id):
        self.model.logs = self.model._load()
        today = date.today().isoformat()
        return [
            l for l in self.model.logs
            if l.user_id == user_id and l.log_date == today
        ]
    
    def delete_by_habit(self, habit_id):
        self.model.logs = [l for l in self.model.logs if l.habit_id != habit_id]
        self.model._save()

    def delete_logs_from_habit(self, habit_id):
        self.model.delete_by_habit(habit_id)

