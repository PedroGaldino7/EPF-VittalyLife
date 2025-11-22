from app import create_app
from bottle import request, response

if __name__ == '__main__':
    app = create_app()
    app.run()
