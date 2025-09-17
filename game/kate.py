from .Aichaosbrain import AIChaosBrain
from .Beast_bestiary import BeastBestiary
from .Gotcha_fails_system import GotchaFailsSystem
from .Modes_manager import ModesManager
from .characters import Kate, Amya, Holly

class Game:
    def __init__(self, character=Kate(), state=None):
        if state:
            self.score = state['score']
            self.level = state['level']
            self.power_ups = state['power_ups']
            self.character = state['character']
            self.ai_brain = state['ai_brain']
            self.bestiary = state['bestiary']
            self.fails_system = state['fails_system']
            self.modes_manager = state['modes_manager']
            self.output = []
        else:
            self.output = ["The Coliseum rips free, floating. The Chaos Queens rise."]
            self.score = 0
            self.level = 1
            self.power_ups = {
                'jetpack': {'quantity': 1, 'effect': 'You soar through the air on jets of plasma!'},
                'whoopee_cushion': {'quantity': 1, 'effect': 'A comical *PFFFT* distracts your opponent.'}
            }
            self.character = character
            self.ai_brain = AIChaosBrain()
            self.bestiary = BeastBestiary(coins=10)
            self.fails_system = GotchaFailsSystem()
            self.modes_manager = ModesManager()
            self.ai_brain.load_memory()
            self.output.append(f"Welcome, {self.character.name}, the {self.character.trait} Queen. Chaos awaits.")

    def get_state(self):
        return {
            'score': self.score,
            'level': self.level,
            'power_ups': self.power_ups,
            'character': self.character,
            'ai_brain': self.ai_brain,
            'bestiary': self.bestiary,
            'fails_system': self.fails_system,
            'modes_manager': self.modes_manager,
        }

    def switch_character(self, character_name):
        if character_name.lower() == 'kate':
            self.character = Kate()
        elif character_name.lower() == 'amya':
            self.character = Amya()
        elif character_name.lower() == 'holly':
            self.character = Holly()
        else:
            return "Unknown character."
        return f"Switched to {self.character.name}, the {self.character.trait} Queen."

    def check_level_up(self):
        if self.modes_manager.xp >= self.level * 100:
            self.level += 1
            self.output.append(f"**** LEVEL UP! You are now Level {self.level}. ****")
            self.bestiary.coins += 5
            self.output.append("**** You earned 5 coins! ****")

    def game_loop_turn(self, player_action):
        self.output = [f"--- Your action: {player_action} ---"]
        self.ai_brain.learn_move(player_action)
        twist_message = self.ai_brain.throw_twist()
        self.output.append(f"AI: {twist_message}")
        if "AI adapts" not in twist_message:
            self.score += 50
            self.output.append(f"** Score +50 for AI twist! Total Score: {self.score} **")

        if player_action == "use ability":
            ability_message = self.character.special_ability()
            self.output.append(ability_message)
            self.score += 75
            self.output.append(f"** Score +75 for special ability! Total Score: {self.score} **")
        elif player_action.startswith("use_powerup"):
            try:
                powerup_name = player_action.split(" ")[1]
                if self.power_ups.get(powerup_name) and self.power_ups[powerup_name]['quantity'] > 0:
                    self.power_ups[powerup_name]['quantity'] -= 1
                    self.output.append(self.power_ups[powerup_name]['effect'])
                    self.score += 15
                    self.output.append(f"** Score +15 for using a power-up! Total Score: {self.score} **")
                else:
                    self.output.append(f"No {powerup_name} power-up available!")
            except IndexError:
                self.output.append("Invalid command. Use 'use_powerup [name]'.")
        elif player_action.startswith("switch_character"):
            try:
                char_name = player_action.split(" ")[1]
                switch_message = self.switch_character(char_name)
                self.output.append(switch_message)
            except IndexError:
                self.output.append("Invalid switch_character command. Use 'switch_character [name]'.")
        elif player_action == "ride beast":
            if not self.bestiary.owned_beasts:
                self.output.append("You have no beasts! Let's buy one...")
                buy_message = self.bestiary.buy_beast('leo_lion')
                self.output.append(buy_message)
            if self.bestiary.owned_beasts:
                ride_message = self.bestiary.ride_beast(self.bestiary.owned_beasts[0])
                self.output.append(ride_message)
                self.score += 25
                self.output.append(f"** Score +25 for riding a beast! Total Score: {self.score} **")
        elif player_action == "fail":
            fail_message = self.fails_system.add_fail("You tripped on a cosmic banana peel.")
            self.output.append(fail_message)
            self.score -= 10
            self.output.append(f"** Score -10 for failing! Total Score: {self.score} **")
        elif player_action.startswith("switch_mode"):
            try:
                mode = player_action.split(" ")[1]
                mode_message = self.modes_manager.switch_mode(mode)
                self.output.append(mode_message)
            except IndexError:
                self.output.append("Invalid switch_mode command. Use 'switch_mode [mode]'.")
        else:
            if self.modes_manager.current_mode == 'therapy':
                if player_action == 'create':
                    self.output.append("You sculpt a beautiful, shimmering star out of cosmic dust.")
                    self.score += 5
                    self.output.append(f"** Score +5 for creating! Total Score: {self.score} **")
                elif player_action == 'reflect':
                    self.output.append("You sit by a holographic waterfall, finding a moment of peace.")
                    self.score += 5
                    self.output.append(f"** Score +5 for reflecting! Total Score: {self.score} **")
                else:
                    self.output.append(f"In Therapy Mode, you gently redirect your '{player_action}' energy into a peaceful hum.")
            else:
                xp_message = self.modes_manager.earn_xp(player_action)
                self.output.append(xp_message)
                self.score += 10
                self.output.append(f"** Score +10 for action! Total Score: {self.score} **")
        self.check_level_up()
        self.output.append("--- Turn End ---")
        return self.output
