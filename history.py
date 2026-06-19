from save_manager import SaveManager


class MatchHistory:

    def __init__(self):

        self.history = SaveManager.load(
            "history.json",
            []
        )


    def add_match(self, result, score):

        self.history.append(
            {
                "result": result,
                "score": score
            }
        )

        SaveManager.save(
            "history.json",
            self.history
        )


    def show(self):

        print("\n===== MATCH HISTORY =====")

        for i, match in enumerate(self.history, start=1):

            print(
                f"{i}. {match['result']} | Score : {match['score']}"
            )