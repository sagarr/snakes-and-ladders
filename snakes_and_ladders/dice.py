import random


class Dice:

    def throw(self):
        return random.randint(1, 6)


class CrookedDice:

    def __init__(self):
        self.dice = Dice()

    def throw(self):
        number = self.dice.throw()
        while number % 2 != 0:
            number = self.dice.throw()

        return number
