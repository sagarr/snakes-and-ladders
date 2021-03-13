class Board:

    def __init__(self, board_size=100):
        self.player_position = 1
        self.board_size = board_size

    def move(self, dice_thrown):
        if self.player_position + dice_thrown <= self.board_size:
            self.player_position += dice_thrown

        return self.player_position
