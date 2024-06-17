"""Main module of the program."""

from Athena import Athena
from User import User


if __name__ == "__main__":
    Athena(User.User({})).main_loop()
