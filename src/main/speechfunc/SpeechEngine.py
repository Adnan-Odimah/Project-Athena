"""Main class for the audio engine of Project Athena"""

import subprocess
import pygame

from features import MusicPlayer as mp



class SpeechEngine:
    """Main class for the audio engine of Project Athena"""

    def __init__(self, config: dict) -> None:
        self.settings = config["settings"]
        self.user_info = config["user_info"]

        self.music_player = mp.MusicPlayer()

        self.currently_playing = None

        self.voice = self.settings["voice"]

        pygame.init()
        pygame.mixer.init()

        self.initialise()

    def initialise(self):
        """Function to initialise the audio engine"""

        self.music_channel = pygame.mixer.Channel(0)
        self.alarms_channel = pygame.mixer.Channel(2)

        pygame.mixer.music.set_volume(self.settings["volume"])

        self.music_channel.set_volume(self.settings["volume"])

        if self.settings["volume"] >= 0.1:
            self.alarms_channel.set_volume(self.settings["volume"])
        else:
            self.alarms_channel.set_volume(0.5)

    def speak(self, text: str) -> None:
        """Says the text that was passed into the function

        Args:
            text (str): The text to be said by the selected voice
        """
        command = (
            'edge-tts --voice "'
            + self.voice
            + f'" --text "{text}" --write-media sounds/temp.mp3'
        )

        # Execute the TTS command
        subprocess.run(command, shell=True, check=True)

        try:
            self.music_channel.set_volume(0.1)
            self.alarms_channel.set_volume(0.1)

            # Load the audio file
            pygame.mixer.music.load("audio/sounds/temp.mp3")

            # Play the audio file
            pygame.mixer.music.play()

            # Wait for the audio playback to finish
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Clean up: unload the audio file
            pygame.mixer.music.unload()
            self.alarms_channel.set_volume(self.settings["volume"])
            self.music_channel.set_volume(self.settings["volume"])

    def play(self, song: str = None) -> None:
        """Play the song that was passed into the function or skip if no song is passed

        Args:
            song (str, optional): Song to be played. Defaults to None.

        Raises:
            type: Error getting music.
        """
        if song:  # If a song is passed into the function
            self.music_player.q_song(song)

            if self.currently_playing:  # If a song is already playing
                return
        try:
            song = self.music_player.get_next()

        except Exception as e:
            raise type(e)(f"An error occurred: {e}") from e

        self.currently_playing = song

        song = pygame.mixer.Sound(song)
        self.music_channel.play(song)

    def pause(self) -> None:
        """Pauses the current song"""
        if self.music_channel.get_busy():
            self.music_channel.pause()
        else:
            self.music_channel.unpause()
