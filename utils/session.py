from bottle import request, response
from config import Config

def set_session_user(user_id):
    response.set_cookie("user_id", str(user_id), secret=Config.SECRET_KEY, path="/")

def get_session_user():
    return request.get_cookie("user_id", secret=Config.SECRET_KEY)

def clear_session():
    response.delete_cookie("user_id", path="/")