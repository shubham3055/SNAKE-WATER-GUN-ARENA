import random


class DragonEmperor:

    def __init__(self):

        self.name = "🐉 Dragon Emperor"
        self.hp = 20

    def attack(self):

        attacks = [

            "Fire Breath 🔥",
            "Shadow Strike ⚫",
            "Ice Blast ❄",
            "Dragon Roar 🐲"

        ]

        return random.choice(attacks)

    def damage(self):

        self.hp -= 1