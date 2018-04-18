from string import ascii_uppercase

class Solver:
    def __init__(self, board):
        self.board = board
        self.boardSize = int(pow(len(board), 0.5))
        self.boxSize = int(pow(self.boardSize, 0.5))
        self.rows = ascii_uppercase[:self.boardSize]    #Cells are identified by Keys A1, A2...

    def print_board(self, algo, board = None):
        if board == None:
            board = self.board
        n = self.boardSize        # length and breadth of board

        result = ""

        for row in self.rows:
            for col in range(1, n + 1):
                key = row + str(col)
                result = result + str((board[key].value))

        with open('output.txt', 'w+') as f:
            f.write(result + " " + algo)
        f.close()


    def is_solved(self):
        n = self.boardSize
        for row in self.rows:
            for col in range(1, n + 1):
                key = row + str(col)
                if self.board[key].value == 0:
                    return False
        return True


