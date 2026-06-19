from rich.console import Console
from rich.panel import Panel

from game import Game
from statistics import Statistics
from history import MatchHistory
from leaderboard import LeaderBoard
from achievements import AchievementManager
from shop import Shop
from inventory import Inventory

console = Console()


def menu():

    game = Game()

    stats = Statistics()
    history = MatchHistory()
    leaderboard = LeaderBoard()
    achievements = AchievementManager()

    shop = Shop(game.player)
    inventory = Inventory()

    while True:

        console.print(
            Panel.fit(
"""
🐍 SNAKE WATER GUN ARENA X

1. Play Game
2. Tournament Mode
3. Boss Battle
4. Survival Mode
5. Story Mode
6. Statistics
7. Match History
8. Leaderboard
9. Achievements
10. Shop
11. Inventory
12. Profile
13. Exit
""",
title="MAIN MENU"
            )
        )

        choice = input("\nChoose : ")

        if choice == "1":

            game.start()

        elif choice == "2":

            print("\n🏟 Tournament Mode Coming Soon...")

        elif choice == "3":

            print("\n👑 Boss Battle Coming Soon...")

        elif choice == "4":

            print("\n🔥 Survival Mode Coming Soon...")

        elif choice == "5":

            print("\n🌌 Story Mode Coming Soon...")

        elif choice == "6":

            print("\n📊 STATISTICS")

            for key, value in stats.data.items():

                print(
                    f"{key.replace('_',' ').title()} : {value}"
                )

        elif choice == "7":

            history.show()

        elif choice == "8":

            leaderboard.display()

        elif choice == "9":

            achievements.show()

        elif choice == "10":

            shop.menu()

        elif choice == "11":

            inventory.show()

        elif choice == "12":

            game.player.show_profile()

        elif choice == "13":

            console.print(
                "\n[bold cyan]Thanks For Playing Snake Water Gun Arena X 👋[/bold cyan]"
            )

            break

        else:

            console.print(
                "[bold red]Invalid Choice![/bold red]"
            )


if __name__ == "__main__":

    menu()