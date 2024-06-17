""" Contains the Alarm class. """

from datetime import datetime
import pygame


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
        self.timeToRing = context['time']
        self.date #TODO:
        self.sound = "sounds/" + config[] #TODO:

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
