class Player:
    def __init__(self, name="ChaosQueen"):
        self.name = name
        self.heartbeat = 80  # Normal resting heartbeat

    def update_heartbeat(self, new_beat):
        self.heartbeat = new_beat
        print(f"Heartbeat updated to: {self.heartbeat} bpm")

    def get_heartbeat(self):
        return self.heartbeat
