class Game:

    def __init__(self, board, dice):
        self.board = board
        self.dice = dice
        self.winner_player = -1

    def play(self, player_turn):
        dice_thrown = self.dice.throw()
        position = self.board.move(dice_thrown)
        print(f"Dice {dice_thrown} thrown by Player {player_turn} and moved to position {position} on board!")
        if position == 100:  # FIXME board size hardcoded
            self.winner_player = player_turn
            print(f"{player_turn} WON!!")

    def winner(self):
        return self.winner_player
