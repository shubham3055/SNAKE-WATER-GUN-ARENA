class SecretCodes:

    codes = {
        "GODMODE":1000,
        "LEGEND":500,
        "DRAGON":250,
        "SHUBHAM":5000
    }

    def redeem(self, code, player):

        code = code.upper()

        if code in self.codes:

            player.coins += self.codes[code]

            print("🎁 Reward Claimed!")

        else:

            print("❌ Invalid Code")