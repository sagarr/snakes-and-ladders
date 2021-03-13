from snakes_and_ladders.board import Board


def test_default_board_size():
    board = Board()
    assert board.board_size == 100


def test_initial_position_of_player_on_board():
    board = Board()
    assert board.player_position == 1


def test_player_move_by_dice_thrown():
    board = Board()

    # TODO can be parametrized
    assert board.move(1) == 2
    assert board.move(1) == 3
    assert board.move(2) == 5
    assert board.move(6) == 11
    assert board.move(5) == 16
    assert board.move(4) == 20


def test_player_can_not_move_out_of_board():
    board = Board()

    # HACK: throw dice of 98
    board.move(98)

    # dice other than 1 will not advance the board
    assert board.move(6) == 99
    assert board.move(3) == 99
    assert board.move(1) == 100  # WON
    assert board.move(2) == 100  # Already WON, won't advance
