import random

class BeastBestiary:
    def __init__(self, coins=0):
        self.coins = coins
        self.beasts = {
            'leo_lion': {'cost': 1, 'effect': 'Roar shakes chest – haptic thunder!'},
            'scorpio_sting': {'cost': 1, 'effect': 'Cosmic slap – buzz in your hand!'},
            'taurus_bull': {'cost': 2, 'effect': 'Charge forward – ground quakes under feet.'},
            'phoenix': {'cost': 5, 'effect': 'Rise from plasma – warm glow on skin.'},
            'knight_mount': {'cost': 10, 'effect': 'Legendary knight: Customize plasma armor, win the Chaos Crown!'}
        }
        self.owned_beasts = []

    def buy_beast(self, beast_name):
        if beast_name in self.beasts and self.coins >= self.beasts[beast_name]['cost']:
            self.coins -= self.beasts[beast_name]['cost']
            self.owned_beasts.append(beast_name)
            return f"Beast acquired: {self.beasts[beast_name]['effect']} Sons' stars flare!"
        else:
            return "Not enough coins, queen. Raid a village!"

    def ride_beast(self, beast_name):
        if beast_name in self.owned_beasts:
            zodiac_boost = random.choice(['Leo roars', 'Scorpio stings', 'Libra balances'])
            return f"Riding {beast_name}! {zodiac_boost} – feel the jolt in your spine."
        return "No beast? Buy one first!"

# Usage: bestiary = BeastBestiary(5); print(bestiary.buy_beast('leo_lion')); print(bestiary.ride_beast('leo_lion'))
