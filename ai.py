import random

class AI:

    def __init__(self,difficulty="easy"):
        self.difficulty=difficulty
        self.history=[]

    def move(self):

        if self.difficulty=="easy":
            return random.choice(["s","w","g"])

        elif self.difficulty=="medium":

            if len(self.history)<3:
                return random.choice(["s","w","g"])

            most=max(set(self.history),key=self.history.count)

            counter={
                "s":"g",
                "g":"w",
                "w":"s"
            }

            return counter[most]

        return random.choice(["s","w","g"])