""" Listens for audio input and returns the text that was spoken """

import speech_recognition as sr


def listen_for_audio(mode: int) -> str:
    """Listens for audio input and returns the text that was spoken in the appropriate mode

    Args:
        mode (int): mode of listening (0 always on, 1 wake word, 2 mute)

    Returns:
        str: The text the user said
    """
    if mode == 2:
        return
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise before listening
        recognizer.adjust_for_ambient_noise(source)

        # Listen for audio input
        audio = recognizer.listen(source)

    try:
        # Use the recognizer to convert speech to text
        text = recognizer.recognize_google(audio)

        if mode == 1:
            if "Athena" in text:
                return text
            else:
                return ""

        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
    return ""
