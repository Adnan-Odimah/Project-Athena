class User:
    """A class to represent a user"""

    def __init__(self, data: dict) -> None:
        self.name = data["name"] if "name" in data else None
        self.birthday = data["birthday"] if "birthday" in data else None
        self.location = data["location"] if "location" in data else None
        self.email = data["email"] if "email" in data else None
        self.phone = data["phone"] if "phone" in data else None
        self.os = data["os"] if "os" in data else None
        self.preferences = (
            data["preferences"]
            if "preferences" in data
            else {
                "voice": "en-GB-SoniaNeural",
                "volume": 0.5,
                "humour": ("dad", 0.0),
                "sarcasm": 0.0,
                "disabled": [],
                "mode": 1,
                "alarm": "default.mp3",
            }
        )

    def get_config(self) -> dict:
        """Returns the config dictionary of the user

        Returns:
            dict: The config data in the form of a dictionary
        """
        config = {
            "user_info": {
                "name": self.name,
                "birthday": self.birthday,
                "location": self.location,
                "email": self.email,
                "phone": self.phone,
                "os": self.os,
            },
            "settings": self.preferences,
        }
        return config
