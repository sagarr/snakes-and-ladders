from snakes_and_ladders.board import SnakeBoard
from snakes_and_ladders.dice import Dice
from snakes_and_ladders.game import Game


def test_simulate_game_play():
    game = Game(SnakeBoard(snake_positions=[(14, 7), (56, 35), (91, 24)]), Dice())

    # play until we get winner
    while game.winner() == -1:
        game.play(0)


def test_play_start_with_first_palyer_alwasy():
    pass


def test_player_playing_in_turns():
    players = ["Ajay", "Sagar"]
    game = Game(players, SnakeBoard(players=len(players), snake_positions=[(14, 7), (56, 35), (91, 24)]), Dice())

    print("-----------")
    while game.winner() == -1:
        game.play()


# Support N players
# they play in turn
