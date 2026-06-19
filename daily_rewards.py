from datetime import datetime
from save_manager import SaveManager


class DailyReward:

    def __init__(self):

        self.data = SaveManager.load(
            "daily_reward.json",
            {
                "last_claim": ""
            }
        )

    def claim(self, player):

        today = str(datetime.now().date())

        if self.data["last_claim"] != today:

            self.data["last_claim"] = today

            player.coins += 200

            SaveManager.save(
                "daily_reward.json",
                self.data
            )

            print("\n🎁 Daily Reward Claimed!")
            print("+200 Coins")

        else:

            print("\nAlready claimed today.")