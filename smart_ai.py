import random
from collections import Counter


class SmartAI:

    def __init__(self):
        self.history = []

    def move(self):

        if len(self.history) < 3:
            return random.choice(["s", "w", "g"])

        most_used = Counter(self.history).most_common(1)[0][0]

        counter = {
            "s": "g",
            "g": "w",
            "w": "s"
        }

        return counter[most_used]

    def record(self, player_move):
        self.history.append(player_move)