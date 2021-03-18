import pytest

from snakes_and_ladders.board import SnakeBoard


def test_snake_start_position_greater_than_end_position_on_board():
    snake_board = SnakeBoard(snake_positions=[(14, 7)])

    for snake_start_pos, snake_end_pos in snake_board.get_snake_positions():
        assert snake_start_pos > snake_end_pos


def test_duplicate_snake_start_position_not_allowed_on_board():
    with pytest.raises(ValueError):
        SnakeBoard(snake_positions=[(14, 7), (14, 1)])


# TODO parametrized tests for various start and end positions
def test_snake_bite_moves_player_from_snake_start_position_to_end_position():
    snake_board = SnakeBoard(snake_positions=[(14, 7)])

    snake_board.move(6, 0)  # 7
    snake_board.move(6, 0)  # 13

    player_position = snake_board.move(1, 0)  # 14

    assert player_position == 7
