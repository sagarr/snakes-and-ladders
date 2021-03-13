class Board:

    def __init__(self, board_size=100):
        self.player_position = 1
        self.board_size = board_size

    def move(self, dice_thrown):
        if self.player_position + dice_thrown <= self.board_size:
            self.player_position += dice_thrown

        return self.player_position


class SnakeBoard:

    def __init__(self, snake_positions):
        self.board = Board()
        self.snake_positions = {}
        for start_pos, end_pos in snake_positions:
            if start_pos in self.snake_positions:
                raise ValueError(f"Snake already placed at {start_pos}!")
            self.snake_positions[start_pos] = end_pos

    def get_snake_positions(self):
        for start_pos, end_pos in self.snake_positions.items():
            yield start_pos, end_pos

    def move(self, dice_thrown):
        player_position = self.board.move(dice_thrown)

        if player_position in self.snake_positions:
            # player moved to snake start position, descend to snake end position
            end_position = self.snake_positions[player_position]
            player_position = self.board.move(end_position - player_position)

        return player_position
