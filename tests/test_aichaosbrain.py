import unittest
from unittest.mock import patch, mock_open
import sys
import os
import json

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Aichaosbrain import AIChaosBrain

class TestAIChaosBrain(unittest.TestCase):

    def setUp(self):
        """Set up a new AIChaosBrain instance before each test."""
        self.brain = AIChaosBrain()

    def test_initialization(self):
        """Test that the AIChaosBrain initializes with default values."""
        self.assertEqual(self.brain.player_moves, [])
        self.assertEqual(self.brain.fears, ['sandstorm', 'floating_islands', 'dance_or_die'])
        self.assertEqual(self.brain.memory_file, 'chaos_memory.json')

    @patch('Aichaosbrain.AIChaosBrain.save_memory')
    def test_learn_move(self, mock_save_memory):
        """Test learning a player move."""
        self.brain.learn_move('attack')
        self.assertEqual(self.brain.player_moves, ['attack'])
        mock_save_memory.assert_called_once()

    @patch('Aichaosbrain.AIChaosBrain.save_memory')
    def test_learn_move_limit(self, mock_save_memory):
        """Test that the move list is capped at 10."""
        for i in range(15):
            self.brain.learn_move(f'move_{i}')
        self.assertEqual(len(self.brain.player_moves), 10)
        self.assertEqual(self.brain.player_moves[0], 'move_5')
        self.assertEqual(self.brain.player_moves[9], 'move_14')

    def test_throw_twist_dodge(self):
        """Test the twist when 'dodge' is a recent move."""
        self.brain.player_moves = ['attack', 'jump', 'dodge']
        response = self.brain.throw_twist()
        self.assertTrue(any(fear in response for fear in ["Dance for a shield", "Sudden sandstorm", "Floating islands"]))

    def test_throw_twist_no_dodge(self):
        """Test the default twist."""
        self.brain.player_moves = ['attack', 'jump', 'run']
        response = self.brain.throw_twist()
        self.assertEqual(response, "AI adapts: Basic roar from Leo. Feel it rumble.")

    @patch('json.dump')
    @patch("builtins.open", new_callable=mock_open)
    def test_save_memory(self, mock_file, mock_json_dump):
        """Test saving memory to a file."""
        self.brain.player_moves = ['attack', 'dodge']
        self.brain.save_memory()
        mock_file.assert_called_once_with('chaos_memory.json', 'w')
        mock_json_dump.assert_called_once_with({'moves': ['attack', 'dodge']}, mock_file())

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({'moves': ['test_move']}))
    def test_load_memory(self, mock_file):
        """Test loading memory from a file."""
        self.brain.load_memory()
        self.assertEqual(self.brain.player_moves, ['test_move'])
        mock_file.assert_called_once_with('chaos_memory.json', 'r')

    @patch("builtins.open", new_callable=mock_open)
    def test_load_memory_file_not_found(self, mock_file):
        """Test loading memory when the file doesn't exist."""
        mock_file.side_effect = FileNotFoundError
        self.brain.load_memory()
        self.assertEqual(self.brain.player_moves, [])


if __name__ == '__main__':
    unittest.main()
