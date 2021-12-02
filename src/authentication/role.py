from authentication.middleware import Middleware


class UserRole(Middleware):
    def __init__(self, server):
        super(Middleware).__init__()
        self._nextHandler = None
        self._server = server

    def handle(self, user):
        role = self._server.getRole(user.getEmail())
        if role is None:
            return False

        print("Hello ", role)
        return super(UserRole, self).handle(user)