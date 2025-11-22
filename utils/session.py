from bottle import request, response

def set_session_user(user_id):
    response.set_cookie("user_id", str(user_id), path="/")

def get_session_user():
    return request.get_cookie("user_id")

def clear_session():
    response.delete_cookie("user_id", path="/")
