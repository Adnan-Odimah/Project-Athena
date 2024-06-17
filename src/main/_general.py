""" Contains general functions used for ease of life in other aspects of athena"""

from datetime import datetime, timedelta


def get_next_weekday(
    target_weekday_str,
):  # TODO: ADD PROPER WAY TO HANDLE INPUTTED DATES
    """
    Returns the date of the next specified weekday.

    Parameters:
    target_weekday_str (str): The target weekday as a string (e.g., "Monday", "Tuesday")

    Returns:
    datetime.date: The date of the next specified weekday
    """
    # Mapping of weekday names to their corresponding integers
    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

    # Convert the target weekday string to the corresponding integer
    target_weekday = weekdays.get(target_weekday_str.capitalize())
    if target_weekday is None:
        raise ValueError("Invalid weekday name")

    today = datetime.now()
    days_ahead = target_weekday - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    next_weekday = today + timedelta(days=days_ahead)
    return next_weekday.date()


def context_to_datetime(context: dict) -> datetime:
    time = context["time"]

    if "next" in context["date"]:
        date = get_next_weekday(context["date"])

    elif "":
        pass
