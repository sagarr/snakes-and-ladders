from snakes_and_ladders.dice import Dice, CrookedDice


def test_normal_dice_throw_numbers_between_1to6():
    dice = Dice()

    for _ in range(100):
        assert dice.throw() in [1, 2, 3, 4, 5, 6]
        assert dice.throw() not in [0, 7, 8, 99]


def test_crooked_dice_throw_even_numbers_only():
    dice = CrookedDice()

    for _ in range(100):
        assert dice.throw() in [2, 4, 6]
        assert dice.throw() not in [1, 3, 5]
