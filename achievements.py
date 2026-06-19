from save_manager import SaveManager


class AchievementManager:

    def __init__(self):

        self.achievements = SaveManager.load(
            "achievements.json",
            []
        )


    def unlock(self, achievement):

        if achievement not in self.achievements:

            self.achievements.append(achievement)

            SaveManager.save(
                "achievements.json",
                self.achievements
            )

            print(f"\n🏆 Achievement Unlocked : {achievement}")