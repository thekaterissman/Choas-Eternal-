import random
import os
from google.cloud import firestore

class BeastBestiary:
    def __init__(self, user_id="default_user", initial_coins=0):
        self.beasts = {
            'leo_lion': {'cost': 1, 'effect': 'Roar shakes chest – haptic thunder!'},
            'scorpio_sting': {'cost': 1, 'effect': 'Cosmic slap – buzz in your hand!'},
            'taurus_bull': {'cost': 2, 'effect': 'Charge forward – ground quakes under feet.'},
            'phoenix': {'cost': 5, 'effect': 'Rise from plasma – warm glow on skin.'},
            'knight_mount': {'cost': 10, 'effect': 'Legendary knight: Customize plasma armor, win the Chaos Crown!'}
        }
        self.owned_beasts = []
        self.coins = initial_coins
        self.user_id = user_id

        # --- Google Cloud Firestore Integration ---
        try:
            self.db = firestore.Client()
            # Each user gets their own document in the 'bestiary_state' collection
            self.doc_ref = self.db.collection('bestiary_state').document(self.user_id)
        except Exception as e:
            self.db = None
            print(f"Warning: Could not connect to Firestore. Beast Bestiary state will not be persisted. Error: {e}")
        # -----------------------------------------

    def load_state(self):
        """Loads the user's state from Firestore."""
        if not self.db:
            return

        try:
            doc = self.doc_ref.get()
            if doc.exists:
                data = doc.to_dict()
                self.coins = data.get('coins', self.coins)
                self.owned_beasts = data.get('owned_beasts', [])
            else:
                # If no document exists, save the initial state to create one
                self.save_state()
        except Exception as e:
            print(f"Error loading bestiary state from Firestore: {e}")

    def save_state(self):
        """Saves the user's state to Firestore."""
        if not self.db:
            return

        state = {
            'user_id': self.user_id,
            'coins': self.coins,
            'owned_beasts': self.owned_beasts
        }
        try:
            self.doc_ref.set(state, merge=True)
        except Exception as e:
            print(f"Error saving bestiary state to Firestore: {e}")

    def buy_beast(self, beast_name):
        if beast_name in self.beasts and self.coins >= self.beasts[beast_name]['cost']:
            self.coins -= self.beasts[beast_name]['cost']
            self.owned_beasts.append(beast_name)
            self.save_state()  # Persist state after purchase
            return f"Beast acquired: {self.beasts[beast_name]['effect']} Sons' stars flare!"
        else:
            return "Not enough coins, queen. Raid a village!"

    def ride_beast(self, beast_name):
        if beast_name in self.owned_beasts:
            zodiac_boost = random.choice(['Leo roars', 'Scorpio stings', 'Libra balances'])
            return f"Riding {beast_name}! {zodiac_boost} – feel the jolt in your spine."
        return "No beast? Buy one first!"

# Usage:
# bestiary = BeastBestiary(user_id="player123", initial_coins=5)
# bestiary.load_state()
# print(bestiary.buy_beast('leo_lion'))
# print(bestiary.ride_beast('leo_lion'))
