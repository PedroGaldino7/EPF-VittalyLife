from bottle import Bottle, request
from controllers.base_controller import BaseController
from services.user_service import UserService


class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    def list_users(self):
        current_user = self.get_logged_user()

        if not current_user or not current_user.is_admin:
            return self.redirect('/dashboard')

        users = self.user_service.get_all()
        return self.render('users', users=users)

    def add_user(self):
        current_user = self.get_logged_user()

        if not current_user or not current_user.is_admin:
            return self.redirect('/dashboard')

        if request.method == 'GET':
            return self.render("criar_usuario")

        self.user_service.save()
        return self.redirect('/users')

    def edit_user(self, user_id):
        current_user = self.get_logged_user()

        if not current_user:
            return self.redirect('/login')

        if not current_user.is_admin and current_user.id != user_id:
            return self.redirect('/dashboard')

        user = self.user_service.get_by_id(user_id)

        if request.method == 'GET':
            return self.render("editar_usuario", user=user, logged_user=current_user)

        self.user_service.edit(user)
        return self.redirect('/users' if current_user.is_admin else '/dashboard')

    def delete_user(self, user_id):
        current_user = self.get_logged_user()

        if not current_user or not current_user.is_admin:
            return self.redirect('/dashboard')

        self.user_service.delete(user_id)
        return self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
