class LoyaltyProgram:
    """
    Represents a guest's loyalty program with points and tier status.
    """

    def __init__(self, guest, points: int = 0, tier: str = "Bronze"):
        self.__guest = guest
        self.__points = points
        self.__tier = tier

    def redeem_points(self, amount: int) -> bool:
        if self.__points >= amount:
            self.__points -= amount
            return True
        return False

    def check_rewards(self) -> str:
        return f"{self.__points} points available. Current tier: {self.__tier}"

    def update_points(self, points: int):
        self.__points += points
        self.update_tier()

    def update_tier(self):
        if self.__points >= 1000:
            self.__tier = "Gold"
        elif self.__points >= 500:
            self.__tier = "Silver"
        else:
            self.__tier = "Bronze"

    def __str__(self):
        return self.check_rewards()