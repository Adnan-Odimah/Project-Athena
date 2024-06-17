""" Main file for Athena program that puts all the pieces together"""

import features
from NLP import Context
from NLP.IntentClassification import commandRecognition
from User import User
from speechfunc import SpeechEngine, listener
from features import Alarm
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
        print(req_type)
        if req_type == "ALARM":
            context = self.context_model.get_reminders_context(request)
            self.running.append(Alarm.Alarm((context), self.user.get_config()))
            self.speechEng.speak(
                f"Set up an alarm at {context['time']} on {context['date']} for {context['task']}"
            )
            if context["frequency"] is not None:
                self.speechEng.speak(f"The alarm will repeat {context['frequency']}")

    def background(self):  ## CHANGE THIS
        while True:
            time.sleep(1)
