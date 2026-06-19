from inventory import Inventory


class Shop:

    def __init__(self, player):

        self.player = player
        self.inventory = Inventory()

    def menu(self):

        while True:

            print("\n🛒 SHOP")
            print("Coins :", self.player.coins)

            print("""
1. Shield (100)
2. Heal (75)
3. Double Damage (150)
4. Freeze Enemy (200)
5. Exit
""")

            choice = input("Choose : ")

            if choice == "1":

                if self.player.coins >= 100:

                    self.player.coins -= 100
                    self.inventory.add_item("shield")

                    print("Shield Purchased!")

                else:

                    print("Not enough coins!")

            elif choice == "2":

                if self.player.coins >= 75:

                    self.player.coins -= 75
                    self.inventory.add_item("heal")

            elif choice == "3":

                if self.player.coins >= 150:

                    self.player.coins -= 150
                    self.inventory.add_item("double_damage")

            elif choice == "4":

                if self.player.coins >= 200:

                    self.player.coins -= 200
                    self.inventory.add_item("freeze")

            else:

                break