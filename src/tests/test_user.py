import unittest


import sys
sys.path.append('c:\\Users\\adnan\\Dropbox\\Coding Projects\\Python\\Project Athena\\src') # Adjust the path accordingly
from main.User.User import User



class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            "name": "John Doe",
            "birthday": "1990-01-01",
            "location": "New York",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "os": "Windows"
        }
        self.user = User(self.user_data)

    def test_user_creation(self):
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.birthday, "1990-01-01")
        self.assertEqual(self.user.location, "New York")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertEqual(self.user.phone, "123-456-7890")
        self.assertEqual(self.user.os, "Windows")

    def test_user_config(self):
        config = self.user.get_config()
        expected_config = {
            "user_info": {
                "name": "John Doe",
                "birthday": "1990-01-01",
                "location": "New York",
                "email": "john.doe@example.com",
                "phone": "123-456-7890",
                "os": "Windows"
            },
            "settings": {
                "voice": "en-GB-SoniaNeural",
                "volume": 0.5,
                "humour": ("dad", 0.0),
                "sarcasm": 0.0,
                "disabled": [],
                "mode": 1,
            }
        }
        self.assertEqual(config, expected_config)