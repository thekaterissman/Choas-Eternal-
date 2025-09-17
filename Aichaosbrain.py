import random
import json  # For saving "memories"
from Player import Player
from Lighting_manager import LightingManager

class AIChaosBrain:
    def __init__(self):
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']  # Your nightmares
        self.memory_file = 'chaos_memory.json'  # Persists across runs
        self.player = Player()
        self.lighting_manager = LightingManager()

    def learn_move(self, move):
        self.player_moves.append(move)
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]  # Keep recent
        self.save_memory()

    def throw_twist(self):
        # Default heartbeat
        self.player.update_heartbeat(80)

        if 'dodge' in self.player_moves[-3:]:  # If you're dodging a lot...
            twist = random.choice(self.fears)

            if twist == 'dance_or_die':
                self.player.update_heartbeat(140)
                self.lighting_manager.sync_with_heartbeat(self.player.get_heartbeat())
                return "AI whispers: Dance for a shield, or get wrecked! Groove time."
            elif twist == 'sandstorm':
                self.player.update_heartbeat(160)
                self.lighting_manager.sync_with_heartbeat(self.player.get_heartbeat())
                return "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury."
            else:
                self.player.update_heartbeat(180)
                self.lighting_manager.sync_with_heartbeat(self.player.get_heartbeat())
                return "Floating islands spawn—gravity flips! Stomach drop incoming."
        else:
            self.player.update_heartbeat(100)
            self.lighting_manager.sync_with_heartbeat(self.player.get_heartbeat())
            return "AI adapts: Basic roar from Leo. Feel it rumble."

    def save_memory(self):
        memory = {'moves': self.player_moves}
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)

    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
                self.player_moves = memory.get('moves', [])
        except FileNotFoundError:
            pass  # Fresh chaos

# Usage: brain = AIChaosBrain(); brain.load_memory(); print(brain.throw_twist())
