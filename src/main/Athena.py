""" Main file for Athena program that puts all the pieces together"""

import features
from NLP import Context
from NLP.IntentClassification import commandRecognition
from User import User
from speechfunc import SpeechEngine
import multiprocessing as mp


class Athena:
    def __init__(self, user: User):
        self.mode = user.preferences["mode"]
        self.user = user

    def main_loop(self):
        while True:  # TODO: CHANGE THIS!
            p
