from authentication.user import User

class Server:
    def __init__(self):
        self.users = {}
        self.middleware = None

    def setMiddleware(self, middleware):
        self.middleware = middleware

    def register(self, email, password, role):
        self.users[email] = {}
        self.users[email]["password"] = password
        self.users[email]["role"] = role

    def logIn(self, email, password):
        user = User(email, password)
        if self.middleware.handle(user):
            print("Authorized access")
            return True
        return False

    def getRole(self, email):
        role = self.users[email]["role"]
        return role

    def hasEmail(self, email):
        return email in self.users

    def isValidPassword(self, email, password):
        if email in self.users:
            return password == self.users[email]["password"]