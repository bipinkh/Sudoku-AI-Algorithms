from copy import deepcopy
from solver.Board import Board
from solver.ArcConsistency import AC3
from solver.Backtrack import BTS
import sys

if __name__ == "__main__":

    #get the unsolved mystery string
    mysteryProblem = sys.argv[1]

    #lets generate the board
    boardObj = Board(mysteryProblem)
    board = boardObj.sudoku_board()

    # check if AC3 can solve it
    ac3 = AC3(deepcopy(board))
    ac3Board = ac3.using_AC3()
    if ac3Board and ac3.is_solved():
        ac3.print_board(algo="AC3")

    # well, if AC3 cannot solve it then let's make a try with BTS
    else:

        bts = BTS(deepcopy(ac3Board))
        btsBoard = bts.using_BTS()
        if btsBoard and bts.is_solved():
            bts.print_board(algo="BTS")


        #and, if both cannot solve it, then the board does not have any solution
        else:
            print("This puzzle has no solution")