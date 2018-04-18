from string import ascii_uppercase
from solver.Cell import Cell

class Board:

    #initialize with the string of cells associated with this board
    def __init__(self, sudokuString):
        self.sudokuString = sudokuString

    def sudoku_board(self):

        # here we can literally solve sudoku of any size. so, to be sure what length of sudoku string
        # user has entered, we calculate the length and then generate rowList, columnList and board accordingly

        length = int(pow(len(self.sudokuString), 0.5))  #length or breadth of board

        rowList = ascii_uppercase[:length]
        index = 0

        Board = {}                        #dictionary to represent "Cell notation" as KEY and "Cell Value" as VALUE

        for row in rowList:                                #cell = [value, domain]
          for column in range (1, length+1):
              key = row + str(column)

              cell = Cell()     # let's get Cell object for each cell of our board

              # if the value is initially not empty fill it as given, or else leave it as 0
              if self.sudokuString[index] != '0':
                  cell.value = int(self.sudokuString[index])
                  cell.domain = {cell.value}

            #now assign the cell to the key in dictionary
              Board[key] = cell
              index += 1
        return Board