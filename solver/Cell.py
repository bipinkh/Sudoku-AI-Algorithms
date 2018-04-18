# this here represents the initial value of any cell to be empty or say 0
# then the domain of the cell is from 0 to 9

class Cell:
    def __init__(self):
        #set initially the cell as empty
        self.value = 0
        #set the domain from 1 to 9
        self.domain = {1, 2, 3, 4, 5, 6, 7, 8, 9}