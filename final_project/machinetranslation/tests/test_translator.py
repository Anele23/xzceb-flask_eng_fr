"""Translator Test Script."""
import unittest
from translator import english_to_french,french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Class that contains tests methods for English to French.
    """
    def test1(self):
        """
        Method to test English to French.
        """
        self.assertNotEqual(english_to_french("Hello"),None)
        self.assertEqual(english_to_french("Hello"),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    """
    Class that contains tests methods for French to English.
    """
    def test1(self):
        """
        Method to test French to English.
        """
        self.assertNotEqual(french_to_english("Bonjour"),None)
        self.assertEqual(french_to_english("Bonjour"),'Hello')

unittest.main()