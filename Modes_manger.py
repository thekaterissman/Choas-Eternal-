import random
import os
from google.cloud import firestore

class ModesManager:
    def __init__(self, user_id="default_user"):
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []  # Persist builds
        self.user_id = user_id

        # --- Google Cloud Firestore Integration ---
        try:
            self.db = firestore.Client()
            self.doc_ref = self.db.collection('modes_manager_state').document(self.user_id)
        except Exception as e:
            self.db = None
            print(f"Warning: Could not connect to Firestore. Modes Manager state will not be persisted. Error: {e}")
        # -----------------------------------------

    def load_state(self):
        """Loads the user's state from Firestore."""
        if not self.db:
            return

        try:
            doc = self.doc_ref.get()
            if doc.exists:
                data = doc.to_dict()
                self.current_mode = data.get('current_mode', self.current_mode)
                self.xp = data.get('xp', self.xp)
                self.shelters = data.get('shelters', [])
            else:
                # If no document exists, save the initial state to create one
                self.save_state()
        except Exception as e:
            print(f"Error loading modes manager state from Firestore: {e}")

    def save_state(self):
        """Saves the user's state to Firestore."""
        if not self.db:
            return

        state = {
            'user_id': self.user_id,
            'current_mode': self.current_mode,
            'xp': self.xp,
            'shelters': self.shelters
        }
        try:
            self.doc_ref.set(state, merge=True)
        except Exception as e:
            print(f"Error saving modes manager state to Firestore: {e}")

    def switch_mode(self, mode):
        modes = ['hunter', 'survival', 'pvp', 'raid']
        if mode in modes:
            self.current_mode = mode
            self.save_state()  # Persist state change
            if mode == 'survival':
                return "Survival Mode: Craft vines to blades. XP sticks – no resets!"
            elif mode == 'pvp':
                return "PvP: Teams self-select. Mix crews, clash in the arena!"
            elif mode == 'raid':
                return "Raid villages! Steal loot, burn down – haptics make walls crack."
            else:
                return "Hunter Mode: Self-pick teams. Hunt or be hunted."
        return "Invalid mode – chaos only!"

    def earn_xp(self, action):
        xp_gain = random.randint(10, 50)
        self.xp += xp_gain
        if self.current_mode == 'survival':
            self.shelters.append('new_shelter')  # Build persists
        self.save_state()  # Persist state change
        return f"XP +{xp_gain}! Total: {self.xp}. Boosts Coliseum skills."

    def mix_modes(self, mode1, mode2):
        return f"Mixed: {mode1} + {mode2} = Pure dive! Remake world in 5s."

# Usage:
# manager = ModesManager(user_id="player123")
# manager.load_state()
# print(manager.switch_mode('survival'))
# print(manager.earn_xp('raid'))
