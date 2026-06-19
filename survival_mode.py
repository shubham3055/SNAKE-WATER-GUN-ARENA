import random


class SurvivalMode:

    def start(self):

        wave = 1

        while True:

            print("\n🌊 Wave", wave)

            enemy_hp = wave

            while enemy_hp > 0:

                move = input("s/w/g : ")

                enemy_move = random.choice(["s", "w", "g"])

                print("Enemy :", enemy_move)

                enemy_hp -= 1

            wave += 1

            again = input("\nContinue? (y/n): ")

            if again != "y":
                break

        print("\n🏆 Highest Wave :", wave)