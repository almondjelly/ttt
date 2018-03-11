class Player(object):

    def __init__(self, name, game_piece):
        self.name = name
        self.game_piece = game_piece


class Move(object):

    def __init__(self, author, position):
        self.author = author
        self.position = position


class Board(object):

    def __init__(self):
        self.moves = []
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    def display(self):
        for row in self.board:
            print row[0], row[1], row[2]
            print

    def add_move(self, move):
        self.moves.append(move)


class Game(object):

    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        # self.started_at =
        # self.finished_at =


def create_player(name, game_piece):
    player = Player(name, game_piece)
    return player

#
#
#
print "Yay! Let's play tic tac toe!"
playerX_name = raw_input("Player X, what's your name? ")
playerX = create_player(playerX_name, "X")

playerO_name = raw_input("Player O, what's your name? ")
playerO = create_player(playerO_name, "O")

board = Board()
board.display()

X_move = raw_input("{}, what's your move? ".format(playerX.name))
X_move.replace(" ", "")
X_move = tuple(X_move)
first_move = Move(playerX, X_move)

board.add_move(first_move)
# board.board[first_move[0]][first_move[1]]
board.display()
board.board[first_move.position[0]][first_move.position[1]] = 'X'