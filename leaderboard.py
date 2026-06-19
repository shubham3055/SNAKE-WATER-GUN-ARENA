from save_manager import SaveManager


class LeaderBoard:

    def __init__(self):

        self.players = SaveManager.load(
            "leaderboard.json",
            []
        )


    def add_player(self, name, wins):

        self.players.append(
            {
                "name": name,
                "wins": wins
            }
        )

        self.players.sort(
            key=lambda x: x["wins"],
            reverse=True
        )

        SaveManager.save(
            "leaderboard.json",
            self.players
        )


    def display(self):

        print("\n🏆 LEADERBOARD")

        for i, player in enumerate(
                self.players[:10],
                start=1):

            print(
                f"{i}. {player['name']} - {player['wins']} wins"
            )