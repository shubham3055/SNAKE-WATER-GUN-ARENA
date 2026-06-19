class RankSystem:

    def get_rank(self, wins):

        if wins >= 100:
            return "👑 God"

        elif wins >= 50:
            return "💎 Diamond"

        elif wins >= 25:
            return "🥇 Gold"

        elif wins >= 10:
            return "🥈 Silver"

        return "🥉 Bronze"