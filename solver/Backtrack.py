from  solver.Solver import Solver
from solver.ArcConsistency import AC3
from copy import deepcopy
import operator

class BTS(Solver):
    def __init__(self, board):
        Solver.__init__(self, board)

    def select_unassigned_variable(self, currentBoard):           #using MRV
        n = self.boardSize
        mrv = None; minLength = 10
        for row in self.rows:
            for col in range(1, n + 1):
                key = row + str(col)
                l = len(currentBoard[key].domain)
                if l > 1 and l < minLength:
                    mrv = key; minLength = l
        return mrv

    def select_value(self, variable, currentBoard):                #using LCV
        n = self.boardSize
        row = variable[0]
        col = int(variable[1])
        lcv = {}; neighbours = set()
        for value in currentBoard[variable].domain:
            count = 0
            for c in range(1, n + 1):
                if c != col:
                    nodeK = row + str(c)
                    if self.board[nodeK].value == 0 and nodeK not in neighbours:
                        if value in self.board[nodeK].domain:
                            count += 1
                            neighbours.add(nodeK)
            for r in self.rows:
                if r != row:
                    nodeK = r + str(col)
                    if self.board[nodeK].value == 0:
                        if value in self.board[nodeK].domain and nodeK not in neighbours:
                            count += 1
                            neighbours.add(nodeK)
            boxColumn = int((col - 1) / self.boxSize) * self.boxSize  # box arcs
            boxRow = int((self.rows.index(row)) / self.boxSize) * self.boxSize
            for r in self.rows[boxRow:boxRow + self.boxSize]:
                for c in range(boxColumn + 1, boxColumn + self.boxSize + 1):
                    nodeK = r + str(c)
                    if self.board[nodeK].value == 0 and nodeK not in neighbours:
                        if value in self.board[nodeK].domain:
                            count += 1
                            neighbours.add(nodeK)
            lcv[value] = count
        temp = sorted(lcv.items(), key=operator.itemgetter(1))
        lcvList = [val[0] for val in temp]
        return list(reversed(lcvList))

    def backtrack(self, board):
        variable = self.select_unassigned_variable(board)
        if variable is None:
            self.board = board
            return board
        for value in self.select_value(variable, board):
            currentBoard = deepcopy(board)
            currentBoard[variable].value = value
            currentBoard[variable].domain = {value}
            infer = AC3(currentBoard)
            inference = infer.using_AC3()
            if inference:
                result = self.backtrack(inference)
                if result:
                    return result
        return False

    def using_BTS(self):
        return self.backtrack(deepcopy(self.board))
