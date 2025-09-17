import random

class BeastBestiary:
    def __init__(self, coins=0):
        self.coins = coins
        self.beasts = {
            'leo_lion': {
                'cost': 1,
                'effect': 'Roar shakes chest – haptic thunder!',
                'lore': 'Ancient stargazers saw this constellation as the Nemean Lion, slain by Hercules. Its roar was said to shatter armor.'
            },
            'scorpio_sting': {
                'cost': 1,
                'effect': 'Cosmic slap – buzz in your hand!',
                'lore': 'The scorpion that battled Orion the hunter now forever chases him across the night sky. Its sting is cosmic justice.'
            },
            'taurus_bull': {
                'cost': 2,
                'effect': 'Charge forward – ground quakes under feet.',
                'lore': 'This is the Cretan Bull, a creature of moonlight and madness. Zeus himself rode it across the sea.'
            },
            'phoenix': {
                'cost': 5,
                'effect': 'Rise from plasma – warm glow on skin.',
                'lore': 'A symbol of rebirth, the Phoenix lives for 1,000 years before dissolving into ash and rising anew. Its tears can heal.'
            },
            'knight_mount': {
                'cost': 10,
                'effect': 'Legendary knight: Customize plasma armor, win the Chaos Crown!',
                'lore': 'Knights of the Round Table sought the Holy Grail. Here, you seek the Chaos Crown, a treasure of equal legend.'
            }
        }
        self.owned_beasts = []

    def buy_beast(self, beast_name):
        beast = self.beasts.get(beast_name)
        if beast and self.coins >= beast['cost']:
            self.coins -= beast['cost']
            self.owned_beasts.append(beast_name)
            return f"Beast acquired: {beast['effect']} Sons' stars flare!\nLore: {beast['lore']}"
        else:
            return "Not enough coins, queen. Raid a village!"

    def ride_beast(self, beast_name):
        if beast_name in self.owned_beasts:
            zodiac_boost = random.choice(['Leo roars', 'Scorpio stings', 'Libra balances'])
            lore = self.beasts[beast_name]['lore']
            return f"Riding {beast_name}! {zodiac_boost} – feel the jolt in your spine.\nAncient Echo: {lore}"
        return "No beast? Buy one first!"

# Usage:
bestiary = BeastBestiary(15)
print(bestiary.buy_beast('leo_lion'))
print(bestiary.buy_beast('phoenix'))
print(bestiary.ride_beast('leo_lion'))
