class Game:

    def __init__(self, players, board, dice):
        self.players = players
        self.player_turn = 0
        self.board = board
        self.dice = dice
        self.winner_player = ""

    def play(self):
        if self.player_turn == len(self.players):
            self.player_turn = 0

        dice_thrown = self.dice.throw()
        position = self.board.move(dice_thrown, self.player_turn)
        print(f"Dice {dice_thrown} thrown by Player {self.players[self.player_turn]} and "
              f"moved to position {position} on board!")
        if position == self.board.size:
            self.winner_player = self.players[self.player_turn]
            print(f"{self.winner_player} WON!!")

        self.player_turn += 1

    def has_winner(self):
        return self.winner_player != ""
