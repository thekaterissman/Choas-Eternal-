import unittest
import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modes_manger import ModesManager

class TestModesManager(unittest.TestCase):

    def setUp(self):
        """Set up a new ModesManager instance before each test."""
        self.manager = ModesManager()

    def test_initialization(self):
        """Test that the ModesManager initializes with default values."""
        self.assertEqual(self.manager.current_mode, 'hunter')
        self.assertEqual(self.manager.xp, 0)
        self.assertEqual(self.manager.shelters, [])

    def test_switch_mode_valid(self):
        """Test switching to a valid mode."""
        response = self.manager.switch_mode('survival')
        self.assertEqual(self.manager.current_mode, 'survival')
        self.assertIn("Survival Mode", response)

        response = self.manager.switch_mode('pvp')
        self.assertEqual(self.manager.current_mode, 'pvp')
        self.assertIn("PvP", response)

        response = self.manager.switch_mode('raid')
        self.assertEqual(self.manager.current_mode, 'raid')
        self.assertIn("Raid villages", response)

        response = self.manager.switch_mode('hunter')
        self.assertEqual(self.manager.current_mode, 'hunter')
        self.assertIn("Hunter Mode", response)

    def test_switch_mode_invalid(self):
        """Test switching to an invalid mode."""
        response = self.manager.switch_mode('creative')
        self.assertEqual(self.manager.current_mode, 'hunter') # Should not change
        self.assertEqual(response, "Invalid mode – chaos only!")

    def test_earn_xp_normal_mode(self):
        """Test earning XP in a non-survival mode."""
        initial_xp = self.manager.xp
        response = self.manager.earn_xp('some_action')
        self.assertTrue(self.manager.xp > initial_xp)
        self.assertIn("XP +", response)
        self.assertEqual(len(self.manager.shelters), 0)

    def test_earn_xp_survival_mode(self):
        """Test earning XP in survival mode, which should add a shelter."""
        self.manager.switch_mode('survival')
        initial_xp = self.manager.xp
        initial_shelters = len(self.manager.shelters)
        response = self.manager.earn_xp('crafting')
        self.assertTrue(self.manager.xp > initial_xp)
        self.assertEqual(len(self.manager.shelters), initial_shelters + 1)
        self.assertIn("XP +", response)

    def test_mix_modes(self):
        """Test the mix_modes method."""
        response = self.manager.mix_modes('survival', 'pvp')
        self.assertEqual(response, "Mixed: survival + pvp = Pure dive! Remake world in 5s.")

if __name__ == '__main__':
    unittest.main()
