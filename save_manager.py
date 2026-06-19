import json
import os

class SaveManager:

    @staticmethod
    def load(filename, default):

        path = f"data/{filename}"

        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump(default, f, indent=4)

        with open(path, "r") as f:
            return json.load(f)


    @staticmethod
    def save(filename, data):

        path = f"data/{filename}"

        with open(path, "w") as f:
            json.dump(data, f, indent=4)