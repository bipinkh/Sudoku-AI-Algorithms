from string import ascii_uppercase
from solver.Cell import Cell

class Board:
    def __init__(self, sudokuString):
        self.sudokuString = sudokuString

    def sudoku_board(self):
        n = int(pow(len(self.sudokuString), 0.5))          #length or breadth of board
        rowList = ascii_uppercase[:n]
        index = 0
        Board = {}                                         #Board = {A1: Cell, A2: cell}...  Dictionary
        for row in rowList:                                #cell = [value, domain]
          for col in range (1, n+1):
              key = row + str(col)
              cell = Cell()
              if self.sudokuString[index] != '0':
                  cell.value = int(self.sudokuString[index])
                  cell.domain = {cell.value}
              Board[key] = cell
              index += 1
        return Board