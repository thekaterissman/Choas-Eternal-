import random
import json
import os
from google.cloud import storage

class AIChaosBrain:
    def __init__(self, user_id="default_user"):
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']  # Your nightmares
        self.memory_file = f'chaos_memory_{user_id}.json'  # User-specific memory file

        # --- Google Cloud Storage Integration ---
        # IMPORTANT: Set the GCS_BUCKET_NAME environment variable to your bucket name.
        bucket_name = os.environ.get('GCS_BUCKET_NAME')
        if bucket_name:
            self.storage_client = storage.Client()
            self.bucket = self.storage_client.bucket(bucket_name)
        else:
            self.bucket = None
            print("Warning: GCS_BUCKET_NAME environment variable not set. AI memory will not be persisted.")
        # -----------------------------------------

    def learn_move(self, move):
        self.player_moves.append(move)
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]  # Keep recent
        self.save_memory()

    def throw_twist(self):
        if 'dodge' in self.player_moves[-3:]:  # If you're dodging a lot...
            twist = random.choice(self.fears)
            if twist == 'dance_or_die':
                return "AI whispers: Dance for a shield, or get wrecked! Groove time."
            elif twist == 'sandstorm':
                return "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury."
            else:
                return "Floating islands spawn—gravity flips! Stomach drop incoming."
        else:
            return "AI adapts: Basic roar from Leo. Feel it rumble."

    def save_memory(self):
        if not self.bucket:
            return  # Do not save if bucket is not configured

        memory = {'moves': self.player_moves}
        blob = self.bucket.blob(self.memory_file)
        try:
            # Upload the memory dictionary as a JSON string
            blob.upload_from_string(
                json.dumps(memory, indent=2),
                content_type='application/json'
            )
        except Exception as e:
            print(f"Error saving memory to Google Cloud Storage: {e}")

    def load_memory(self):
        if not self.bucket:
            return  # Do not load if bucket is not configured

        blob = self.bucket.blob(self.memory_file)
        try:
            if blob.exists():
                memory_data = blob.download_as_string()
                memory = json.loads(memory_data)
                self.player_moves = memory.get('moves', [])
        except Exception as e:
            # If there's an error (e.g., permissions), start with fresh chaos
            print(f"Error loading memory from Google Cloud Storage: {e}")
            pass

# Usage:
# brain = AIChaosBrain(user_id="player123")
# brain.load_memory()
# brain.learn_move('dodge')
# print(brain.throw_twist())
