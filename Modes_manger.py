import random

class ModesManager:
    def __init__(self):
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []
        self.blending_recipes = {
            ('pvp', 'survival'): "The Spartan Agoge: You and your shield-brothers must survive the wilds and each other. Only the strongest will return.",
            ('hunter', 'raid'): "The Viking Longship: Your crew hunts for glory and riches. Raid the coastal villages, but beware the local warriors.",
            ('raid', 'survival'): "The Fall of Troy: The city is burning. Survive the chaos, pillage what you can, and escape the wrath of the gods."
        }

    def switch_mode(self, mode):
        modes = ['hunter', 'survival', 'pvp', 'raid']
        if mode in modes:
            self.current_mode = mode
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
            self.shelters.append('new_shelter')
        return f"XP +{xp_gain}! Total: {self.xp}. Boosts Coliseum skills."

    def blend_modes_with_meaning(self, mode1, mode2):
        key = tuple(sorted((mode1, mode2)))
        if key in self.blending_recipes:
            return f"Mode Blend: {self.blending_recipes[key]}"
        else:
            # A default message if the combination is not found
            return f"Mixed: {mode1} + {mode2} = Pure chaos! A new world is born."

# Usage:
manager = ModesManager()
print(manager.switch_mode('survival'))
print(manager.earn_xp('crafting'))
print(manager.blend_modes_with_meaning('survival', 'pvp'))
print(manager.blend_modes_with_meaning('hunter', 'survival'))
