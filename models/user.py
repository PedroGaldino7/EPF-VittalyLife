import json
import os
from datetime import datetime


class User:
    def __init__(self, id, username, email, password_hash, created_at=None, habits=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at or datetime.now().isoformat()
        self.habits = habits or []

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at,
            "habits": self.habits
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class UserModel:
    FILE_PATH = "./data/users.json"

    def __init__(self):
        self.users = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, "r", encoding="utf-8") as f:
            return [User.from_dict(u) for u in json.load(f)]

    def _save(self):
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)

    def get_all(self):
        self.users = self._load()
        return self.users


    def get_by_id(self, user_id):
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
