""" Main file for Athena program that puts all the pieces together"""

import features
from NLP import Context
from NLP.IntentClassification import commandRecognition
from User import User
from speechfunc import SpeechEngine, listener
import threading as th
import time


class Athena:
    def __init__(self, user: User):
        self.mode = user.preferences.get("mode")
        self.user = user
        self.speechEng = SpeechEngine(user.get_config())
        self.running = []
        self.voice = user.preferences.get("voice")
        self.context_model = Context.Context()

    def main_loop(self):
        self.speechEng.speak("Hello, I am Athena, your personal assistant")

        bg_task = th.Thread(target=self.background, name="Background")
        bg_task.start()

        while True:  # TODO: CHANGE THIS!
            self.process_command()

    def process_command(self):
        request = input("enter command:")
        # request = listener.listen_for_audio(self.mode)

        req_type = commandRecognition.classify(request)
        if req_type == "ALARM":
            print(self.context_model.get_reminders_context(request))
            self.speechEng.speak("SET UP ALARM")
            print("SET UP ALARM")

    def background(self):  ## CHANGE THIS
        while True:
            print(time.time())
            time.sleep(1)
