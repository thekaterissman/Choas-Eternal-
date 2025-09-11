class ModesManager:
    def __init__(self):
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []  # Persist builds

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
            self.shelters.append('new_shelter')  # Build persists
        return f"XP +{xp_gain}! Total: {self.xp}. Boosts Coliseum skills."

    def mix_modes(self, mode1, mode2):
        return f"Mixed: {mode1} + {mode2} = Pure dive! Remake world in 5s."

# Usage: manager = ModesManager(); print(manager.switch_mode('survival')); print(manager.earn_xp('raid'))
