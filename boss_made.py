import random


class Boss:

    def __init__(self, name, hp):

        self.name = name
        self.hp = hp

    def attack(self):

        return random.choice(["s", "w", "g"])


class BossBattle:

    def __init__(self):

        self.bosses = [
            Boss("🥉 Bronze Boss", 3),
            Boss("🥈 Silver Boss", 5),
            Boss("🥇 Gold Boss", 7),
            Boss("👹 Shadow King", 10),
            Boss("🐉 Dragon Emperor", 15)
        ]

    def start(self):

        print("\n👑 BOSS MODE")

        for boss in self.bosses:

            print(f"\n⚔ Fighting {boss.name}")
            print(f"❤️ HP : {boss.hp}")

        print("\n🏆 More combat mechanics coming soon...")