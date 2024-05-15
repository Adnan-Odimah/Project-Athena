""" Contains the Timer class. """

from datetime import datetime
import pygame


class Timer:
    """Timer class to handle the timer aspect of Project Athena"""

    def __init__(
        self,
        time_to_ring,
        reason: str = "",
        sound: str = "basic_alarm.mp3",
    ) -> None:
        self.time_to_ring = time_to_ring
        self.channel = pygame.mixer.Channel(2)
        self.reason = reason
        self.sound = "sounds/" + sound

        self.played = False
        self.deleted = False

    def start_check(self) -> str:
        """Checks if the timer should ring

        Returns:
            str: The reason for the timer if it rings, otherwise None.
        """
        if not self.played and not self.deleted:
            if datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ) == self.time_to_ring.strftime("%Y-%m-%d %H:%M:%S"):
                self.ring()
                return self.reason
        return None

    def ring(self):
        """Rings the timer"""
        sound = pygame.mixer.Sound(self.sound)
        self.played = True
        self.channel.play(sound)

    def stop(self):
        """Stops the timer"""
        self.deleted = True
        self.channel.stop()
