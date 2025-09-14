import unittest
import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Gotcha_fails_system import GotchaFailsSystem

class TestGotchaFailsSystem(unittest.TestCase):

    def setUp(self):
        """Set up a new GotchaFailsSystem instance before each test."""
        self.system = GotchaFailsSystem()

    def test_initialization(self):
        """Test that the GotchaFailsSystem initializes with default values."""
        self.assertEqual(self.system.fails_reel, [])
        self.assertEqual(self.system.gotcha_list, [])

    def test_add_fail(self):
        """Test adding a fail to the fails reel."""
        response = self.system.add_fail('epic faceplant')
        self.assertEqual(len(self.system.fails_reel), 1)
        self.assertEqual(self.system.fails_reel[0], 'epic faceplant')
        self.assertIn("Total Fails: epic faceplant", response)

    def test_gotcha_bully(self):
        """Test adding a bully to the gotcha list."""
        response = self.system.gotcha_bully('troll123')
        self.assertEqual(len(self.system.gotcha_list), 1)
        self.assertIn("troll123:", self.system.gotcha_list[0])
        self.assertIn("Gotcha List lights up:", response)


if __name__ == '__main__':
    unittest.main()
