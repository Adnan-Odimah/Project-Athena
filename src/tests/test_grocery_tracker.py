import unittest

import sys
sys.path.append('c:\\Users\\adnan\\Dropbox\\Coding Projects\\Python\\Project Athena\\src\\main') # Adjust the path accordingly
from features import GroceryTracker

class TestGroceryTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = GroceryTracker()

    def test_add_item(self):
        self.tracker.add_item("apples", 5)
        self.assertIn(("apples", 5), self.tracker.grocery_list)

    def test_add_multiple_items(self):
        self.tracker.add_item("apples", 5)
        self.tracker.add_item("bananas", 2)
        self.assertIn(("apples", 5), self.tracker.grocery_list)
        self.assertIn(("bananas", 2), self.tracker.grocery_list)

    def test_add_same_item_increases_quantity(self):
        self.tracker.add_item("apples", 5)
        self.tracker.add_item("apples", 3)
        self.assertIn(("apples", 8), self.tracker.grocery_list)

    def test_remove_item(self):
        self.tracker.add_item("apples", 5)
        self.tracker.remove_item("apples")
        self.assertNotIn(("apples", 5), self.tracker.grocery_list)

    def test_remove_item_specific_quantity(self):
        self.tracker.add_item("apples", 5)
        self.tracker.remove_item("apples", 3)
        self.assertIn(("apples", 2), self.tracker.grocery_list)

    def test_remove_item_more_than_exists(self):
        self.tracker.add_item("apples", 5)
        self.tracker.remove_item("apples", 10)
        self.assertNotIn(("apples", 5), self.tracker.grocery_list)