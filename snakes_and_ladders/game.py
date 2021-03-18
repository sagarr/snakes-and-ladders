
class Game:

    def __init__(self, players, board, dice):
        self.players = players # TODO board
        self.player_turn = 0
        self.board = board
        self.dice = dice
        self.winner_player = -1

    def play(self):
        if self.player_turn == len(self.players):
            self.player_turn = 0

        dice_thrown = self.dice.throw()
        position = self.board.move(dice_thrown, self.player_turn)
        print(f"Dice {dice_thrown} thrown by Player {self.players[self.player_turn]} and moved to position {position} on board!")
        if position == 100:  # FIXME board size hardcoded
            self.winner_player = self.player_turn
            print(f"{self.players[self.player_turn]} WON!!")

        self.player_turn += 1

    def winner(self):
        return self.winner_player
