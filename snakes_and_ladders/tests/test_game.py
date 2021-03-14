from snakes_and_ladders.board import SnakeBoard
from snakes_and_ladders.dice import Dice
from snakes_and_ladders.game import Game


def test_simulate_game_play():
    game = Game(SnakeBoard(snake_positions=[(14, 7), (56, 35), (91, 24)]), Dice())

    # play until we get winner
    while game.winner() == -1:
        game.play(0)
