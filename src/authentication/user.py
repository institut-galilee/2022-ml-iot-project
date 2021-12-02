class User:
    def __init__(self, email, password, role="student"):
        self.email = email
        self.password = password
        self.role = role

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getRole(self):
        return self.role