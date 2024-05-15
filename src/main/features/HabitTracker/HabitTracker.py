""" Contains the class HabitTracker that has all the habits the user has. """

from features.HabitTracker.Habit import Habit


class HabitTracker:
    """The class for the habit tracker"""

    def __init__(self) -> None:
        self.habits = []

    def add_habit(
        self, habit: str, reminder_times: list[str], days_left: int = 30
    ) -> None:
        """Adds a habit to the habit tracker

        Args:
            habit (str): The habit name
            reminder_times (list[str]): The days and times to remind the user
            days_left (int, optional): The amount of days left for the habit to form. Defaults to 30.
        """
        self.habits.append(Habit(habit, reminder_times, days_left))

    def check_habits(self) -> str:
        """Checks if the habits should be reminded

        Returns:
            str: The habit to be reminded
        """
        for habit in self.habits:
            habit.reminder_check()
            return habit.remind()
