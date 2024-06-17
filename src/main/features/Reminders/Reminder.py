"""
This is the Reminder class. It is used to create a reminder object.
"""

from datetime import datetime
from _general import context_to_datetime


class Reminder:
    """Reminder class to handle the reminder aspect of Project Athena"""

    def __init__(self, context: dict) -> None:
        self.date_to_ring = context_to_datetime(context)
        self.context = context

        self.repeat = False

        if context["frequency"] is not None:
            pass  # TODO: ADD NLP processing for when to repeat

        self.played = False
        self.deleted = False

    def ring_check(self) -> str:
        """Checks if its time for the Reminder

        Returns:
            str: The reason for the Reminder if it rings, otherwise None.
        """
        if not self.deleted and self.date_to_ring.strftime(
            "%D/%M/%Y %H:%M"
        ) == datetime.now().strftime("%D/%M/%Y %H:%M"):
            if not self.played:
                self.played = True
                return self.context["task"]

            if not self.repeat:
                self.deleted = True

        self.played = False
        return None

    def stop(self):
        """Stops the Reminder"""
        self.deleted = True
