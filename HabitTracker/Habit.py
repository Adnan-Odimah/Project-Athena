"""
contains the class for each habit
"""

import datetime


class Habit:
    """The class for each habit"""

    def __init__(
        self, habit: str, reminder_times: list[str], days_left: int = 30
    ) -> None:
        """Initialises the habit with the habit name, days and days left.

        Args:
            habit (str): Habit name
            days (list[str]):Days to remind and the time to remind
            days_left (int, optional): amount of days left for the habit to form. Defaults to 30.
        """
        self.habit = habit
        self.days = reminder_times
        self.days_left = days_left

    def reminder_check(self) -> str:
        """Checks if the habit should be reminded

        Returns:
            str: The habit to be reminded
        """
        for day in self.days:
            if day == datetime.datetime.now().strftime("%A %H:%M"):
                self.remind()

    def remind(self) -> str:
        """Reminds the user of the habit

        Returns:
            str: The habit to be reminded
        """
        # TODO: Say the reminder
        # TODO: check input of the user
        done = input(f"Have you done {self.habit} yet? (y/n): ")
        if done == "y":
            self.days_left -= 1
            return f"{self.habit} has been done for the day"
        elif done == "n":
            self.days_left += 1
            return f"{self.habit} has not been done for the day"
