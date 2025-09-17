import random
import json
import os
from google.cloud import storage

class AIChaosBrain:
    def __init__(self):
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']  # Your nightmares
        self.memory_file = 'chaos_memory.json'  # Persists across runs

        # --- Google Cloud Storage Setup ---
        # Instructions:
        # 1. Make sure you have authenticated with Google Cloud CLI: `gcloud auth application-default login`
        # 2. Set the GCS_BUCKET_NAME environment variable to your bucket name:
        #    export GCS_BUCKET_NAME="your-gcs-bucket-name"
        try:
            self.storage_client = storage.Client()
            bucket_name = os.environ.get("GCS_BUCKET_NAME")
            if not bucket_name:
                print("GCS_BUCKET_NAME environment variable not set. Using local file storage.")
                self.bucket = None
            else:
                self.bucket = self.storage_client.bucket(bucket_name)
        except Exception as e:
            print(f"Could not initialize Google Cloud Storage client. Using local file storage. Error: {e}")
            self.bucket = None
        # --- End GCS Setup ---


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
        memory = {'moves': self.player_moves}

        if not self.bucket: # Fallback to local storage
            with open(self.memory_file, 'w') as f:
                json.dump(memory, f)
            return

        blob = self.bucket.blob(self.memory_file)
        blob.upload_from_string(
            data=json.dumps(memory),
            content_type='application/json'
        )


    def load_memory(self):
        if not self.bucket: # Fallback to local storage
            try:
                with open(self.memory_file, 'r') as f:
                    memory = json.load(f)
                    self.player_moves = memory.get('moves', [])
            except FileNotFoundError:
                pass  # Fresh chaos
            return

        blob = self.bucket.blob(self.memory_file)
        if blob.exists():
            try:
                memory_data = blob.download_as_string()
                memory = json.loads(memory_data)
                self.player_moves = memory.get('moves', [])
            except Exception as e:
                print(f"Failed to load memory from GCS: {e}")
        else:
            pass # Fresh chaos, no memory file yet

# Usage: brain = AIChaosBrain(); brain.load_memory(); print(brain.throw_twist())
