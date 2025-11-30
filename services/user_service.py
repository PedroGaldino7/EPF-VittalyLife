from bottle import request
from models.user import UserModel, User
from datetime import datetime
import hashlib


class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        return self.user_model.get_all()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def get_by_id(self, user_id):
        self.user_model.users = self.user_model._load()
        return self.user_model.get_by_id(user_id)
    
    def save(self):
        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1

        username = request.forms.get("username")
        email = request.forms.get("email")
        password = request.forms.get("password")

        password_hash = self.hash_password(password)

        user = User(
            id=new_id,
            username=username,
            email=email,
            password_hash=password_hash,
            created_at=datetime.now().isoformat(),
            habits=[]
        )

        self.user_model.add(user)

    def create_user(self, username, email, password):
        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1

        password_hash = self.hash_password(password)

        user = User(
            id=new_id,
            username=username,
            email=email,
            password_hash=password_hash,
            created_at=datetime.now().isoformat(),
            habits=[]
        )

        self.user_model.add(user)

    def edit(self, user):
        user.username = request.forms.get("username")
        user.email = request.forms.get("email")

        new_password = request.forms.get("password")

        if new_password:
            user.password_hash = self.hash_password(new_password)

        self.user_model.update(user)

    def delete(self, user_id):
        self.user_model.delete(user_id)

        # Apaga todos os hábitos do usuário
        from services.habit_service import HabitService
        HabitService().delete_by_user(user_id)

    def authenticate(self, email, password):
        self.user_model.users = self.user_model._load()

        password_hash = self.hash_password(password)

        for u in self.user_model.users:
            if u.email == email and u.password_hash == password_hash:
                return u

        return None


