from authentication.middleware import Middleware


class UserExist(Middleware):
    def __init__(self, server):
        super(Middleware).__init__()
        self._nextHandler = None
        self._server = server

    def handle(self, user):
        if (not self._server.hasEmail(user.getEmail())):
            print("This email is not registered")
            return False

        if (not self._server.isValidPassword(user.getEmail(), user.getPassword())):
            print("Wrong combination Email/Password")
            return False

        return super(UserExist, self).handle(user)