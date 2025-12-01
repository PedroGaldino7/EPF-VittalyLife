from datetime import datetime
from .base_model import BaseJsonModel

class User:
    def __init__(self, id, username, email, password_hash, created_at=None, is_admin=False):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at or datetime.now().isoformat()
        self.is_admin = is_admin
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at,
            "is_admin": self.is_admin
        }

    @classmethod
    def from_dict(cls, data):
        data['is_admin'] = data.get('is_admin', False)
        return cls(**data)

class UserModel(BaseJsonModel):
    file_path = "./data/users.json"

    def __init__(self):
        raw_data = self._load_data()
        self.users = [User.from_dict(u) for u in raw_data]

    def _save(self):
        self._save_data([u.to_dict() for u in self.users])
    
    def get_all(self):
        raw_data = self._load_data()
        self.users = [User.from_dict(u) for u in raw_data]
        return self.users

    def get_by_id(self, user_id):
        self.get_all()
        return next((u for u in self.users if u.id == user_id), None)

    def add(self, user):
        self.users.append(user)
        self._save()

    def update(self, updated_user):
        for i, u in enumerate(self.users):
            if u.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break

    def delete(self, user_id):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()