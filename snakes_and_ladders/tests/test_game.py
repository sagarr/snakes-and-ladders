from snakes_and_ladders.board import SnakeBoard
from snakes_and_ladders.dice import Dice
from snakes_and_ladders.game import Game


def test_simulate_game_play():
    players = ["Test"]
    game = Game(players, SnakeBoard(players=len(players), snake_positions=[(14, 7), (56, 35), (91, 24)]), Dice())

    # play until we get winner
    while not game.has_winner():
        game.play()


def test_multiplayer():
    players = ["Ajay", "Sagar"]
    game = Game(players, SnakeBoard(players=len(players), snake_positions=[(14, 7), (56, 35), (91, 24)]), Dice())

    while not game.has_winner():
        game.play()
