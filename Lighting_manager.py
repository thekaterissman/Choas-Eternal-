import time

class LightingManager:
    def __init__(self):
        self.current_color = (0, 0, 0)  # Off

    def sync_with_heartbeat(self, heartbeat):
        # Simple mapping: higher heartbeat -> redder light
        red = int(255 * (heartbeat / 180.0))  # Normalize to 0-255
        red = max(0, min(255, red))  # Clamp

        self.current_color = (red, 0, 255 - red)  # Fade from blue to red

        self._pulse(heartbeat)

    def _pulse(self, heartbeat, duration=2.0):
        """Simulates a pulsing light for a given duration."""

        # Calculate pulse timing
        pulse_duration = 60.0 / heartbeat # duration of one beat in seconds

        num_pulses = int(duration / pulse_duration)

        for _ in range(num_pulses):
            # Fade in
            self._fade_to_brightness(1.0, pulse_duration / 2)
            # Fade out
            self._fade_to_brightness(0.5, pulse_duration / 2)

    def _fade_to_brightness(self, target_brightness, duration):
        steps = 15
        delay = duration / steps
        start_brightness = self.get_brightness()

        for i in range(steps + 1):
            ratio = i / steps
            brightness = start_brightness * (1 - ratio) + target_brightness * ratio

            r = int(self.current_color[0] * brightness)
            g = int(self.current_color[1] * brightness)
            b = int(self.current_color[2] * brightness)

            print(f"Lighting: RGB({r}, {g}, {b})")
            time.sleep(delay)

    def get_brightness(self):
        # A simple brightness calculation
        return sum(self.current_color) / (255.0 * 3)

# Usage:
# lm = LightingManager()
# lm.sync_with_heartbeat(120)
