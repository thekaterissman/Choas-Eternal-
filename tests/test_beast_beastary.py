import unittest
import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Beast_beastary import BeastBestiary

class TestBeastBestiary(unittest.TestCase):

    def setUp(self):
        """Set up a new BeastBestiary instance before each test."""
        self.bestiary = BeastBestiary(coins=10)

    def test_initialization(self):
        """Test that the BeastBestiary initializes with default values."""
        self.assertEqual(self.bestiary.coins, 10)
        self.assertEqual(self.bestiary.owned_beasts, [])

    def test_buy_beast_sufficient_coins(self):
        """Test buying a beast with enough coins."""
        response = self.bestiary.buy_beast('leo_lion')
        self.assertEqual(self.bestiary.coins, 9)
        self.assertIn('leo_lion', self.bestiary.owned_beasts)
        self.assertIn("Beast acquired", response)

    def test_buy_beast_insufficient_coins(self):
        """Test buying a beast with not enough coins."""
        bestiary = BeastBestiary(coins=4) # Not enough for a phoenix
        response = bestiary.buy_beast('phoenix') # costs 5
        self.assertEqual(bestiary.coins, 4)
        self.assertNotIn('phoenix', bestiary.owned_beasts)
        self.assertEqual(response, "Not enough coins, queen. Raid a village!")

    def test_buy_beast_non_existent(self):
        """Test buying a beast that does not exist."""
        response = self.bestiary.buy_beast('dragon')
        self.assertEqual(self.bestiary.coins, 10)
        self.assertNotIn('dragon', self.bestiary.owned_beasts)
        self.assertEqual(response, "Not enough coins, queen. Raid a village!")

    def test_ride_beast_owned(self):
        """Test riding a beast that is owned."""
        self.bestiary.buy_beast('taurus_bull')
        response = self.bestiary.ride_beast('taurus_bull')
        self.assertIn("Riding taurus_bull!", response)

    def test_ride_beast_not_owned(self):
        """Test riding a beast that is not owned."""
        response = self.bestiary.ride_beast('phoenix')
        self.assertEqual(response, "No beast? Buy one first!")

if __name__ == '__main__':
    unittest.main()
