import random
import json

class AIChaosBrain:
    def __init__(self):
        self.player_moves = []
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']
        self.memory_file = 'chaos_memory.json'
        self.ancient_wisdom = {
            'sandstorm': "The ancient Egyptians feared sandstorms, believing they were the breath of the chaotic god Set.",
            'floating_islands': "Greek myths tell of Delos, a floating island where the gods Apollo and Artemis were born. It was a sacred, wandering sanctuary.",
            'dance_or_die': "In ancient Greece, the 'Pyrrhic Dance' was a ritual war dance. To dance was to prove your readiness for battle.",
            'default': "The philosopher Heraclitus said, 'The only constant is change.' In the Coliseum, this is law."
        }

    def learn_move(self, move):
        self.player_moves.append(move)
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]
        self.save_memory()

    def throw_twist(self):
        twist_message = "AI adapts: Basic roar from Leo. Feel it rumble."
        wisdom = self.ancient_wisdom['default']

        if 'dodge' in self.player_moves[-3:]:
            twist = random.choice(self.fears)
            wisdom = self.ancient_wisdom.get(twist, self.ancient_wisdom['default'])
            if twist == 'dance_or_die':
                twist_message = "AI whispers: Dance for a shield, or get wrecked! Groove time."
            elif twist == 'sandstorm':
                twist_message = "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury."
            else:
                twist_message = "Floating islands spawn—gravity flips! Stomach drop incoming."

        return f"{twist_message}\nAncient Wisdom: {wisdom}"

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
            pass

# Usage:
brain = AIChaosBrain()
brain.load_memory()
brain.learn_move('dodge')
brain.learn_move('dodge')
brain.learn_move('dodge')
print(brain.throw_twist())
