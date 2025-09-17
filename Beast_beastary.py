import random

class BeastBestiary:
    def __init__(self, coins=0):
        self.coins = coins
        self.beasts = {
            'leo_lion': {'cost': 1, 'effect': 'Roar shakes chest – haptic thunder!', 'color': 'default'},
            'scorpio_sting': {'cost': 1, 'effect': 'Cosmic slap – buzz in your hand!', 'color': 'default'},
            'taurus_bull': {'cost': 2, 'effect': 'Charge forward – ground quakes under feet.', 'color': 'default'},
            'phoenix': {'cost': 5, 'effect': 'Rise from plasma – warm glow on skin.', 'color': 'default'},
            'knight_mount': {'cost': 10, 'effect': 'Legendary knight: Customize plasma armor, win the Chaos Crown!', 'color': 'default_plasma'}
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
            color = self.beasts[beast_name]['color']
            if beast_name == 'knight_mount':
                return f"Riding {beast_name} with {color} plasma armor! {zodiac_boost} – feel the jolt in your spine."
            return f"Riding {beast_name} of color {color}! {zodiac_boost} – feel the jolt in your spine."
        return "No beast? Buy one first!"

    def customize_beast(self, beast_name, color):
        if beast_name in self.owned_beasts:
            self.beasts[beast_name]['color'] = color
            return f"{beast_name} customized with {color} color!"
        return f"You don't own {beast_name} yet. Buy it first!"

# Usage: bestiary = BeastBestiary(5); print(bestiary.buy_beast('leo_lion')); print(bestiary.ride_beast('leo_lion'))
