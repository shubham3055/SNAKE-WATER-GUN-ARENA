import random
from rich.console import Console
from rich.panel import Panel
from player import Player
from ai import AI

console=Console()

class Game:

    def __init__(self):

        self.player=Player(input("Enter Name : "))
        self.ai=AI()

        self.reverse={
            "s":"🐍 Snake",
            "w":"💧 Water",
            "g":"🔫 Gun"
        }

    def result(self,p,c):

        if p==c:
            return 0

        if (p=="s" and c=="w") or\
           (p=="w" and c=="g") or\
           (p=="g" and c=="s"):

            return 1

        return -1

    def start(self):

        while self.player.hp>0:

            console.print(
                Panel.fit(
f"{self.player.name} ❤️"*self.player.hp
                )
            )

            p=input("s/w/g : ")

            c=self.ai.move()

            console.print(self.reverse[p])
            console.print(self.reverse[c])

            r=self.result(p,c)

            if r==1:
                console.print("[green]YOU WIN[/green]")
                self.player.reward()

            elif r==-1:
                console.print("[red]YOU LOST[/red]")
                self.player.damage()

            else:
                console.print("[yellow]DRAW[/yellow]")

        console.print("[bold red]GAME OVER[/bold red]")