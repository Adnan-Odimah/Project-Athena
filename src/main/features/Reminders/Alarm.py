""" Contains the Alarm class. """

# pylint: disable=C0103
from datetime import datetime
import pygame
from _general import get_next_weekday


class Alarm:
    """
    Alarm class to handle the alarm aspect of Project Athena
    """

    def __init__(self, context: dict, config: dict) -> None:
        self.repeat = (
            context["frequency"] if context.get("frequency") is not None else False
        )
        self.channel = pygame.mixer.Channel(2)
        self.reason = context["task"]
        self.timeToRing = context["time"]

        date = get_next_weekday(context["date"])

        self.sound = "sounds/alarms/" + config["settings"]["alarm"]

        self.played = False
        self.deleted = False

    def ring_check(self) -> str:
        """Checks if the alarm should ring

        Returns:
            str: The reason for the alarm if it rings, otherwise None.
        """
        if not self.deleted and not self.played and not self.channel.get_busy():
            for day, time in self.repeat:
                if time.strftime("%H:%M") == datetime.now().strftime(
                    "%H:%M"
                ) and day == datetime.now().strftime("%A"):
                    self.ring()
                    return self.reason
        self.played = False
        return None

    def ring(self):
        """Rings the alarm"""
        sound = pygame.mixer.Sound(self.sound)
        self.played = True
        self.channel.play(sound)

    def stop(self):
        """Stops the alarm"""
        self.deleted = True
        self.channel.stop()
