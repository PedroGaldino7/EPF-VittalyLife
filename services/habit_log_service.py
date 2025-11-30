from datetime import date
from models.habit_log import HabitLogModel, HabitLog

class HabitLogService:
    def __init__(self):
        self.model = HabitLogModel()

    def check_in(self, habit_id, user_id):
        existing = self.model.get_today_by_habit(habit_id, user_id)
        if existing:
            return existing

        new_id = max([l.id for l in self.model.logs], default=0) + 1
        today = date.today().isoformat()

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
        return self.model.get_today_user_logs(user_id)
    
    def delete_logs_from_habit(self, habit_id):
        self.model.delete_by_habit(habit_id)