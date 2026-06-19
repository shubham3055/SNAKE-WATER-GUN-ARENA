import random
import time


class LuckyWheel:

    rewards = [
        "Shield",
        "Double Damage",
        "Heal",
        "100 Coins",
        "Nothing"
    ]

    def spin(self):

        print("\n🎰 SPINNING")

        for i in range(10):

            print(".", end="", flush=True)

            time.sleep(0.2)

        reward = random.choice(self.rewards)

        print("\n\n🎁 Reward :", reward)