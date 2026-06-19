from save_manager import SaveManager


class Statistics:

    def __init__(self):

        self.data = SaveManager.load(
            "stats.json",
            {
                "games_played": 0,
                "wins": 0,
                "losses": 0,
                "draws": 0,
                "longest_streak": 0,
                "coins_earned": 0
            }
        )


    def add_win(self):

        self.data["wins"] += 1
        self.data["games_played"] += 1
        self.save()


    def add_loss(self):

        self.data["losses"] += 1
        self.data["games_played"] += 1
        self.save()


    def add_draw(self):

        self.data["draws"] += 1
        self.save()


    def add_coins(self, amount):

        self.data["coins_earned"] += amount
        self.save()


    def save(self):

        SaveManager.save("stats.json", self.data)