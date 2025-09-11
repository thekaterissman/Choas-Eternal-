import random

class GotchaFailsSystem:
    def __init__(self):
        self.fails_reel = []
        self.gotcha_list = []

    def add_fail(self, fail_desc):
        self.fails_reel.append(fail_desc)
        sound = random.choice(['kazoo solo', 'cosmic chimes', 'fart noise'])
        return f"Total Fails: {fail_desc} – Reel plays with {sound}. Crowd laughs!"

    def gotcha_bully(self, bully_name):
        punishments = ['neon clown face', 'virtual pie SPLAT!', 'holographic shame wave']
        punishment = random.choice(punishments)
        self.gotcha_list.append(f"{bully_name}: {punishment}")
        return f"Gotcha List lights up: {punishment} – Bullies squirm!"

# Usage: system = GotchaFailsSystem(); print(system.add_fail('epic faceplant')); print(system.gotcha_bully('troll123'))
