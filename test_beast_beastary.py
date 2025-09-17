import unittest
from Beast_beastary import BeastBestiary

class TestBeastBestiary(unittest.TestCase):

    def test_customize_knight_mount(self):
        bestiary = BeastBestiary(coins=20)
        bestiary.buy_beast('knight_mount')

        # Test customization
        customization_result = bestiary.customize_beast('knight_mount', 'red_plasma')
        self.assertEqual(customization_result, "knight_mount customized with red_plasma color!")

        # Test riding with custom armor
        ride_result = bestiary.ride_beast('knight_mount')
        self.assertIn("with red_plasma plasma armor!", ride_result)

    def test_customize_leo_lion(self):
        bestiary = BeastBestiary(coins=20)
        bestiary.buy_beast('leo_lion')

        # Test customization
        customization_result = bestiary.customize_beast('leo_lion', 'golden')
        self.assertEqual(customization_result, "leo_lion customized with golden color!")

        # Test riding with custom color
        ride_result = bestiary.ride_beast('leo_lion')
        self.assertIn("of color golden!", ride_result)

    def test_customize_without_owning(self):
        bestiary = BeastBestiary(coins=5)

        # Test customization without owning the beast
        customization_result = bestiary.customize_beast('phoenix', 'fiery_orange')
        self.assertEqual(customization_result, "You don't own phoenix yet. Buy it first!")

if __name__ == '__main__':
    unittest.main()
