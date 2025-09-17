import random
import json  # For saving "memories"

class AIChaosBrain:
    def __init__(self):
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']  # Your nightmares
        self.memory_file = 'chaos_memory.json'  # Persists across runs

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
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)

    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
                self.player_moves = memory.get('moves', [])
        except FileNotFoundError:
            pass  # Fresh chaos

    def tarot_reading(self):
        cards = {
            'The Fool': 'A new beginning, a leap of faith.',
            'The Magician': 'You have the power to manifest your desires.',
            'The High Priestess': 'Trust your intuition and inner knowledge.',
            'The Empress': 'Nurture your creative side and embrace abundance.',
            'The Emperor': 'Take control of your life with structure and authority.',
            'The Hierophant': 'Seek guidance from tradition and trusted advisors.',
            'The Lovers': 'A choice must be made. Follow your heart.',
            'The Chariot': 'Charge forward with determination and willpower.',
            'Strength': 'You have the inner strength to overcome any obstacle.',
            'The Hermit': 'Take time for introspection and soul-searching.',
            'Wheel of Fortune': 'A turning point is near. Embrace change.',
            'Justice': 'Your actions have consequences. Seek balance and fairness.',
            'The Hanged Man': 'Let go of what no longer serves you. A new perspective awaits.',
            'Death': 'An era is ending. Embrace transformation.',
            'Temperance': 'Find harmony and balance in all things.',
            'The Devil': 'Confront your shadow self and break free from bondage.',
            'The Tower': 'A sudden upheaval will bring truth and liberation.',
            'The Star': 'Hope and inspiration are on the horizon.',
            'The Moon': 'Navigate through your fears and illusions.',
            'The Sun': 'Joy, success, and abundance are yours.',
            'Judgement': 'A time of reckoning and rebirth.',
            'The World': 'You have completed a cycle. Celebrate your achievements.'
        }
        card = random.choice(list(cards.keys()))
        return f"The AI deals a card: {card}. Its meaning: '{cards[card]}'"

# Usage:
# brain = AIChaosBrain()
# brain.load_memory()
# print(brain.throw_twist())
# print(brain.tarot_reading())
