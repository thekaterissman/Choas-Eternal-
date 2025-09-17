import random
import os
from google.cloud import firestore

class GotchaFailsSystem:
    def __init__(self, user_id="default_user"):
        self.fails_reel = []
        self.gotcha_list = []
        self.user_id = user_id

        # --- Google Cloud Firestore Integration ---
        try:
            self.db = firestore.Client()
            self.doc_ref = self.db.collection('gotcha_fails_state').document(self.user_id)
        except Exception as e:
            self.db = None
            print(f"Warning: Could not connect to Firestore. Gotcha Fails state will not be persisted. Error: {e}")
        # -----------------------------------------

    def load_state(self):
        """Loads the user's state from Firestore."""
        if not self.db:
            return

        try:
            doc = self.doc_ref.get()
            if doc.exists:
                data = doc.to_dict()
                self.fails_reel = data.get('fails_reel', [])
                self.gotcha_list = data.get('gotcha_list', [])
            else:
                # If no document exists, save the initial state to create one
                self.save_state()
        except Exception as e:
            print(f"Error loading gotcha fails state from Firestore: {e}")

    def save_state(self):
        """Saves the user's state to Firestore."""
        if not self.db:
            return

        state = {
            'user_id': self.user_id,
            'fails_reel': self.fails_reel,
            'gotcha_list': self.gotcha_list
        }
        try:
            self.doc_ref.set(state, merge=True)
        except Exception as e:
            print(f"Error saving gotcha fails state to Firestore: {e}")

    def add_fail(self, fail_desc):
        self.fails_reel.append(fail_desc)
        self.save_state()  # Persist state change
        sound = random.choice(['kazoo solo', 'cosmic chimes', 'fart noise'])
        return f"Total Fails: {len(self.fails_reel)}: {fail_desc} – Reel plays with {sound}. Crowd laughs!"

    def gotcha_bully(self, bully_name):
        punishments = ['neon clown face', 'virtual pie SPLAT!', 'holographic shame wave']
        punishment = random.choice(punishments)
        self.gotcha_list.append(f"{bully_name}: {punishment}")
        self.save_state()  # Persist state change
        return f"Gotcha List lights up: {punishment} – Bullies squirm!"

# Usage:
# system = GotchaFailsSystem(user_id="player123")
# system.load_state()
# print(system.add_fail('epic faceplant'))
# print(system.gotcha_bully('troll123'))
