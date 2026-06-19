class Player:

    def __init__(self, name):

        self.name = name

        # Health
        self.max_hp = 5
        self.hp = 5

        # Economy
        self.coins = 500

        # Statistics
        self.wins = 0
        self.losses = 0
        self.streak = 0

        # Rank and title
        self.rank = "Bronze"
        self.title = "🌱 Beginner"

        # Powers
        self.shield = False
        self.double_damage = False
        self.freeze_enemy = False

    # ---------- HEALTH ----------

    def heal(self):

        if self.hp < self.max_hp:
            self.hp += 1

    def damage(self):

        if self.shield:
            print("🛡 Shield Protected You!")
            self.shield = False
            return

        if self.hp > 0:
            self.hp -= 1

    # ---------- COINS ----------

    def reward(self, amount=50):

        self.coins += amount

    # ---------- MATCH STATS ----------

    def add_win(self):

        self.wins += 1
        self.streak += 1

        self.rank_up()
        self.update_title()

    def add_loss(self):

        self.losses += 1
        self.streak = 0

    # ---------- RANK SYSTEM ----------

    def rank_up(self):

        if self.wins >= 100:
            self.rank = "👑 Legend"

        elif self.wins >= 50:
            self.rank = "💎 Diamond"

        elif self.wins >= 25:
            self.rank = "🥇 Gold"

        elif self.wins >= 10:
            self.rank = "🥈 Silver"

        else:
            self.rank = "🥉 Bronze"

    # ---------- TITLE SYSTEM ----------

    def update_title(self):

        if self.wins >= 100:
            self.title = "🔥 God Of Arena"

        elif self.wins >= 50:
            self.title = "👑 Champion"

        elif self.wins >= 25:
            self.title = "⚔ Warrior"

        elif self.wins >= 10:
            self.title = "🎯 Hunter"

        else:
            self.title = "🌱 Beginner"

    # ---------- HEALTH BAR ----------

    def show_health(self):

        hearts = "❤️" * self.hp
        missing = "🖤" * (self.max_hp - self.hp)

        print()
        print(f"{self.name}")
        print(hearts + missing)
        print()

    # ---------- PROFILE ----------

    def show_profile(self):

        print("\n========== PLAYER PROFILE ==========")
        print(f"👤 Name     : {self.name}")
        print(f"❤️ Health   : {self.hp}/{self.max_hp}")
        print(f"💰 Coins    : {self.coins}")
        print(f"🏆 Wins     : {self.wins}")
        print(f"❌ Losses   : {self.losses}")
        print(f"🔥 Streak   : {self.streak}")
        print(f"🎖 Rank     : {self.rank}")
        print(f"👑 Title    : {self.title}")

        print("\n⚡ Powers")
        print(f"🛡 Shield         : {self.shield}")
        print(f"💥 Double Damage  : {self.double_damage}")
        print(f"❄ Freeze Enemy   : {self.freeze_enemy}")