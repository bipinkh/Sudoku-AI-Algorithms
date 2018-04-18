from solver.Solver import Solver

class AC3(Solver):
    def __init__(self, board):
        Solver.__init__(self, board)
        self.arcQueue = set()

    def add_neighbours(self, nodeI):
        n=self.boardSize
        row = nodeI[0]
        col = int(nodeI[1])
        for c in range(1,n+1):                          #horizontal arcs
            if c != col:
                nodeK = row + str(c)
                if self.board[nodeK].value == 0:
                   self.arcQueue.add((nodeK, nodeI))     #Adding arcs
        for r in self.rows:                              #vartical arcs
            if r != row:
                nodeK = r + str(col)
                if self.board[nodeK].value == 0:
                   self.arcQueue.add((nodeK, nodeI))
        boxColumn = int((col-1)/self.boxSize)*self.boxSize    #box arcs
        boxRow = int((self.rows.index(row))/self.boxSize)*self.boxSize
        for r in self.rows[boxRow:boxRow+self.boxSize]:
            for c in range(boxColumn+1, boxColumn+self.boxSize+1):
                nodeK = r+str(c)
                if self.board[nodeK].value == 0:
                   self.arcQueue.add((nodeK, nodeI))

    def generate_arcs(self, row, col, nodeI, n):
        for c in range(1,n+1):                              #horizontal arcs
            if c != col:
                nodeJ = row + str(c)
                if self.board[nodeJ].value != 0:
                   self.arcQueue.add((nodeI, nodeJ))        #Adding arcs
        for r in self.rows:                                 #vartical arcs
            if r != row:
                nodeJ = r + str(col)
                if self.board[nodeJ].value != 0:
                   self.arcQueue.add((nodeI, nodeJ))
        boxColumn = int((col-1)/self.boxSize)*self.boxSize       #box arcs
        boxRow = int((self.rows.index(row))/self.boxSize)*self.boxSize
        for r in self.rows[boxRow:boxRow+self.boxSize]:
            for c in range(boxColumn+1, boxColumn+self.boxSize+1):
                nodeJ = r+str(c)
                if self.board[nodeJ].value != 0:
                   self.arcQueue.add((nodeI, nodeJ))

    def generate_queue(self):
        n = self.boardSize
        for row in self.rows:
            for col in range(1, n + 1):
                key = row + str(col)
                if self.board[key].value == 0:
                    self.generate_arcs(row, col, key, n)

    def revise(self,  arc):
        Xi = self.board[arc[0]]
        Xj = self.board[arc[1]]
        (Xi.domain).discard(Xj.value)
        if len(Xi.domain) == 1:
            Xi.value = (Xi.domain).pop()
            Xi.domain = {Xi.value}
        return True

    def using_AC3(self):
        self.generate_queue()
        while len(self.arcQueue) > 0:
            arc = self.arcQueue.pop()
            if self.revise(arc):
                if len(self.board[arc[0]].domain) == 0:
                    return False
                if len(self.board[arc[0]].domain) == 1:  #Check neighbours for consistency
                    self.add_neighbours(arc[0])
        return self.board

