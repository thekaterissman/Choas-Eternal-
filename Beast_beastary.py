import random
from asset_loader import AssetLoader

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
        self.asset_loader = AssetLoader()
        self.beast_assets = {
            'leo_lion': {'model': 'leo_lion.fbx', 'sound': 'haptic_roar.wav'},
            'scorpio_sting': {'model': 'scorpio_sting.glb', 'sound': None},
        }

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
            print(f"Riding {beast_name}! {zodiac_boost} – feel the jolt in your spine.")

            if beast_name in self.beast_assets:
                assets = self.beast_assets[beast_name]
                if assets['model']:
                    self.asset_loader.load_model(assets['model'])
                if assets['sound']:
                    self.asset_loader.load_sound(assets['sound'])
            else:
                print(f"No assets defined for {beast_name}")

            return f"Finished riding {beast_name}."
        return "No beast? Buy one first!"

if __name__ == '__main__':
    print("--- Testing BeastBestiary ---")
    bestiary = BeastBestiary(10)

    print("\nBuying a lion...")
    buy_message = bestiary.buy_beast('leo_lion')
    print(buy_message)
    assert 'acquired' in buy_message.lower()

    print("\nRiding the lion...")
    ride_message = bestiary.ride_beast('leo_lion')
    print(ride_message)
    assert 'finished riding' in ride_message.lower()

    print("\n--- Test Complete ---")
