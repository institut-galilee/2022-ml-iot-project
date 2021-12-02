import getpass
from authentication.server import Server
from authentication.user_exist import UserExist
from authentication.role import UserRole
from authentication.middleware import Middleware


def main():
    server = Server()
    server.register("hamidi@lipn.fr", "12345", "student")

    middleware = Middleware()
    middleware.setNext(UserExist(server)).setNext(UserRole(server))
    server.setMiddleware(middleware)

    success = False
    while (not success):
        email = input("Email: ...")
        password = getpass.getpass("Password: ...")
        success = server.logIn(email, password)


if __name__ == '__main__':
    main()