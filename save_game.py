from save_manager import SaveManager


class SaveGame:

    def save(self, player):

        data = {

            "name": player.name,
            "wins": player.wins,
            "losses": player.losses,
            "coins": player.coins,
            "rank": player.rank,
            "hp": player.hp

        }

        SaveManager.save(

            "savegame.json",

            data

        )

    def load(self):

        return SaveManager.load(

            "savegame.json",

            {}

        )