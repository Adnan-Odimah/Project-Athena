""" Contains the main function for the PC Automation program. """

import platform
import pyautogui
import pywhatkit


def close_tab() -> None:
    """Closes the current tab"""
    if "Windows" in platform.platform():
        pyautogui.hotkey("ctrl", "w")

    elif "macOS" in platform.platform():
        with pyautogui.hold(["command"]):
            pyautogui.sleep(0.2)
            pyautogui.press("w")

    else:
        print("Unsupported OS")


# TODO: Stream content to a specific platform
def stream_content(content: str, str_platform: str) -> None:
    """Streams the content to the platform"""
    if str_platform == "youtube":
        pywhatkit.playonyt(content)

    elif "Windows" in platform.platform():
        pyautogui.hotkey("win", "s")
        pyautogui.write(str_platform)
        pyautogui.press("enter")

    elif "macOS" in platform.platform():
        with pyautogui.hold(["command"]):
            pyautogui.sleep(0.3)
            pyautogui.press("space")
        pyautogui.sleep(0.2)
        pyautogui.typewrite(str_platform)
        pyautogui.sleep(0.1)
        pyautogui.press("enter")


def open_app(app_name: str) -> None:
    """Opens the app with the given name"""
    if "Windows" in platform.platform():
        pyautogui.hotkey("win", "s")
        pyautogui.write(app_name)
        pyautogui.press("enter")

    elif "macOS" in platform.platform():
        with pyautogui.hold(["command"]):
            pyautogui.sleep(0.2)
            pyautogui.press("space")
            pyautogui.sleep(0.2)
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.1)
        pyautogui.press("enter")

    else:
        print("Unsupported OS")


# TODO: make it close a specific app
def close_app(app_name: str) -> None:
    """Closes the app with the given name"""
    if "Windows" in platform.platform():
        pyautogui.hotkey("alt", "f4")

    elif "macOS" in platform.platform():
        with pyautogui.hold(["command"]):
            pyautogui.sleep(0.2)
            pyautogui.press("q")

    else:
        print("Unsupported OS")


# TODO: make it switch to a specific app
def switch_to_app(app_name: str) -> None:
    """Switches to the app with the given name"""
    if "Windows" in platform.platform():
        pyautogui.hotkey("alt", "tab")

    elif "macOS" in platform.platform():
        with pyautogui.hold(["command"]):
            pyautogui.sleep(0.2)
            pyautogui.press("tab")

    else:
        print("Unsupported OS")


open_app("Chrome")
