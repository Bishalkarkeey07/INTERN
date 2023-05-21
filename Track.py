import random
class Track:
    OBSTACLE = "Obstacle"
    POWER_UP = "Power-up"

    def __init__(self, length):
        self.length = length
        self.track = self.generate_track()

    def generate_track(self):
        track = []
        for _ in range(self.length):
            element = random.choice([None, self.OBSTACLE, self.POWER_UP])
            track.append(element)
        return track


# Example usage
track_length = 10
track = Track(track_length)
print(track.track)
