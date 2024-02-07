class Game:
    def __init__(self, id):
        self.ready = False
        self.id = id
        self.went = [False, False]
        self.moves = [None, None]

    def get_player_move(self, p):
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        self.went[player] = True

