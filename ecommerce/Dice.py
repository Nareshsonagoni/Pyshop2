import random


class Dice:
    def roll(self):
        first_number = random.randint(1, 6)
        second_number = random.randint(1, 6)
        return first_number, second_number


dice = Dice()
dice2 = Dice()
print(dice.roll())
print(dice2.roll())

