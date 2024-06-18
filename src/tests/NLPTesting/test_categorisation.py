import csv
import unittest

import sys
sys.path.append('c:\\Users\\adnan\\Dropbox\\Coding Projects\\Python\\Project Athena\\src\\main') # Adjust the path accordingly
from NLP import classify

class TestCategorisation(unittest.TestCase):
    test_data = csv.reader(open('c:\\Users\\adnan\\Dropbox\\Coding Projects\\Python\\Project Athena\\data\\Categoriser\\test.csv', 'r'))
    print(test_data)