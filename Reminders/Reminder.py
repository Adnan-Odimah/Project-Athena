"""
This is the Reminder class. It is used to create a reminder object that can be used to store reminders.
"""

from datetime import datetime


class Reminder:
    """Reminder class to handle the reminder aspect of Project Athena"""

    def __init__(
        self,
        repeat: list[tuple[str, datetime]],
        reason: str = "",
    ) -> None:
        self.repeat = repeat
        self.reason = reason

        self.played = False
        self.deleted = False

    def ring_check(self) -> str:
        """Checks if its time for the Reminder

        Returns:
            bool or str:
        """
        if not self.deleted and not self.played:
            for day, time in self.repeat:
                if time.strftime("%H:%M") == datetime.now().strftime(
                    "%H:%M"
                ) and day == datetime.now().strftime("%A"):
                    return self.reason
        self.played = False

    def stop(self):
        """Stops the Reminder"""
        self.deleted = True
