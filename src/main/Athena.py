""" Main file for Athena program that puts all the pieces together"""

# pylist: disable = C0103
import threading as th
import time

from NLP import Context
from NLP.IntentClassification import commandRecognition
from User.User import User
from speechfunc import SpeechEngine
from features import Alarm, Timer, Reminder


class Athena:
    """
    Class responsible for handling the different features of athena
    and linking them together
    """

    def __init__(self, user: User):
        self.mode = user.preferences.get("mode")
        self.user = user
        self.speech_eng = SpeechEngine(user.get_config())
        self.running = []
        self.voice = user.preferences.get("voice")
        self.context_model = Context.Context()

    def main_loop(self):
        """The main athena loop, run when starting the program"""
        self.speech_eng.speak("Hello, I am Athena, your personal assistant")

        bg_task = th.Thread(target=self.background, name="Background")
        bg_task.start()

        while True:  # TODO: CHANGE THIS!
            self.process_command()

    def process_command(self):
        """
        Function responsible for taking a command and processing it to do desired action
        """
        request = input("enter command:")
        # request = listener.listen_for_audio(self.mode)

        req_type = commandRecognition.classify(request)

        if req_type == "ALARM":
            self.process_alarm(request)

        elif req_type == "REMINDER":
            self.process_reminder(request)

        elif req_type == "AUTOMATION":
            # TODO:
            pass

        elif req_type == "MUSIC":
            self.process_music(request)

        elif req_type == "WEATHER":
            # TODO:
            pass

        elif req_type == "PROJECT_TRACKER":
            pass

        elif req_type == "HABIT_TRACKER":
            pass

        elif req_type == "TIMER":
            pass

        elif req_type == "CONVERSATION":
            pass

        elif req_type == "SETTINGS":
            pass

    def background(self):  ## CHANGE THIS TODO:
        """Does the background tasks required"""
        while (
            True
        ):  # TODO: MAKE THIS LOOP ONLY HAPPEN WHEN RUNNING ATTRIBUTE HAS THINGS WITHIN IT
            time.sleep(1)

    def process_alarm(self, text: str):
        """Code responsible for processing alarms

        Args:
            text (str): The request made
        """
        context = self.context_model.get_reminders_context(text)
        self.running.append(Alarm(context, self.user.get_config()))
        self.speech_eng.speak(
            f"Set up an alarm at {context['time']} on {context['date']}"
        )
        if context["frequency"] is not None:
            self.speech_eng.speak(f"The alarm will repeat {context['frequency']}")

    def process_reminder(self, text: str):
        """Function responsible for handling reminder commands

        Args:
            text (str): The command
        """
        context = self.context_model.get_reminders_context(text)
        self.running.append(Reminder(context))
        self.speech_eng.speak(
            f"I will remind you to {context['task']} at {context['time']} on {context['date']}"
        )
        if context["frequency"] is not None:
            self.speech_eng.speak(f"The alarm will repeat {context['frequency']}")

    def process_music(self, text: str):
        """Processes a variety of music commands

        Args:
            text (str): The command to be processed
        """
        text = text.lower()
        split_text = text.split()
        for index, word in enumerate(split_text):
            if word == "play":
                self.speech_eng.play(" ".join(split_text[index:]))
                return

            elif word == "pause":
                self.speech_eng.pause()
                return

            elif "stop" == word and "shuffle" in text:
                if self.speech_eng.shuffle():
                    self.speech_eng.shuffle()
                return

            elif "stop" == word:
                self.speech_eng.pause()
                return

            elif "shuffle" == word:
                if not self.speech_eng.shuffle():
                    self.speech_eng.shuffle()
                return

            elif "remove" == word:
                song_to_remove = " ".join(split_text[index:])
                self.speech_eng.remove(song_to_remove)
                return
