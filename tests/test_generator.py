import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from main import OrthodoxBibleQuoteGenerator
from verses import ORTHODOX_BIBLE_VERSES

class TestOrthodoxBibleQuoteGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This runs once before all tests
        cls.root = tk.Tk()
        cls.root.withdraw()  # Hide the main window during tests

    @classmethod
    def tearDownClass(cls):
        # This runs once after all tests
        cls.root.destroy()

    def setUp(self):
        # This runs before each test
        self.app = OrthodoxBibleQuoteGenerator(self.__class__.root)

    def test_initial_window_setup(self):
        """Test that the main window is configured correctly"""
        self.assertEqual(self.app.root.title(), "Orthodox Bible Quote Generator")
        self.assertEqual(self.app.root.geometry(), "600x400")
        self.assertEqual(self.app.root.resizable(), (True, True))

    def test_generate_quote_ui_elements(self):
        """Test that all UI elements exist after generation"""
        self.assertIsNotNone(self.app.title_label)
        self.assertIsNotNone(self.app.quote_frame)
        self.assertIsNotNone(self.app.reference_label)
        self.assertIsNotNone(self.app.quote_text)
        self.assertIsNotNone(self.app.generate_button)

    def test_verse_generation(self):
        """Test that quote generation produces valid output"""
        # Store initial reference text
        initial_reference = self.app.reference_label.cget("text")
        
        # Generate a quote
        self.app.generate_quote()
        
        # Get the new reference and verse text
        new_reference = self.app.reference_label.cget("text")
        verse_text = self.app.quote_text.get("1.0", tk.END).strip()
        
        # Verify changes
        self.assertNotEqual(initial_reference, new_reference)
        self.assertIn(new_reference, [v[0] for v in ORTHODOX_BIBLE_VERSES])
        self.assertGreater(len(verse_text), 0)

    def test_verse_database_integrity(self):
        """Test that all verses in the database are valid"""
        for reference, verse in ORTHODOX_BIBLE_VERSES:
            self.assertIsInstance(reference, str)
            self.assertIsInstance(verse, str)
            self.assertGreater(len(reference), 0)
            self.assertGreater(len(verse), 0)
            self.assertTrue(":" in reference)  # Basic Bible reference format check

if __name__ == "__main__":
    unittest.main()