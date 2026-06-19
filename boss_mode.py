import random
import time


class Boss:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def move(self):
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

    def result(self, player, boss):

        if player == boss:
            return 0

        if (
                (player == "s" and boss == "w")
                or
                (player == "w" and boss == "g")
                or
                (player == "g" and boss == "s")
        ):
            return 1

        return -1

    def start(self):

        for boss in self.bosses:

            print(f"\n⚔ BATTLE AGAINST {boss.name}")

            while boss.hp > 0:

                print(f"{boss.name} HP : {'❤️'*boss.hp}")

                player_move = input("\ns / w / g : ")

                boss_move = boss.move()

                print("Boss chose :", boss_move)

                ans = self.result(player_move, boss_move)

                if ans == 1:

                    boss.hp -= 1
                    print("✅ Hit!")

                elif ans == -1:

                    print("❌ Boss Hit You!")

                else:

                    print("🤝 Draw")

                time.sleep(1)

        print("\n🏆 ALL BOSSES DEFEATED!")