""" Contains the MusicPlayer class to handle the music player aspect of Project Athena """

import os
import queue
from functools import lru_cache
import yt_dlp as youtube_dl


class MusicPlayer:
    """
    MusicPlayer class to handle the music player aspect of Project Athena
    """

    def __init__(self) -> None:
        self.queue = queue.Queue()
        self.ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

    def get_next(self) -> str:
        """gets the next song in the queue"""
        return self.queue.get_nowait()

    @lru_cache
    def fetch_song(self, song_name: str) -> str:
        """Fetches the song from youtube"""
        if not os.path.exists("music"):
            os.makedirs("music")

        self.ydl_opts["outtmpl"] = f"music/{song_name}.mp3"

        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.extract_info(f"ytsearch:{song_name}")
            return f"music/{song_name}.mp3"

    def q_song(self, song: str) -> None:
        """queues a song and fetches it from youtube if not already fetched"""
        song = self.fetch_song(song)
        self.queue.put_nowait(song)

    def clear_q(self) -> None:
        """clears the queue"""
        self.queue = queue.Queue()
