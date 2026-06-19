from save_manager import SaveManager


class Inventory:

    def __init__(self):

        self.items = SaveManager.load(
            "inventory.json",
            {
                "shield": 0,
                "heal": 0,
                "double_damage": 0,
                "freeze": 0
            }
        )

    def add_item(self, item):

        self.items[item] += 1
        self.save()

    def save(self):

        SaveManager.save(
            "inventory.json",
            self.items
        )

    def show(self):

        print("\n🎒 INVENTORY")

        for item, amount in self.items.items():

            print(f"{item} : {amount}")