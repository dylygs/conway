import numpy as np

class Game:

    def printBoard(self):
        print(self.board)

   
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=bool)
        self.printBoard()

    def setCell(self, x, y, val):
        self.board[y, x] = val

    def getCell(self, x, y):
        return self.board[y, x]
    
    def countNeighbors(self, x, y):
        count = 0;
        if y - 1 >= 0:
            count += self.checkThreeRow(x, y - 1)
        if y + 1 < self.height:
            count += self.checkThreeRow(x, y + 1)

        if x - 1 >= 0 and self.getCell(x - 1, y):
            ++count
        if x + 1 < self.width and self.getCell(x + 1, y):
            ++count

        return count
                
    def checkThreeRow(self, x, y):
        count = 0
        if self.getCell(x, y):
            ++count
        if x - 1 >= 0 and self.getCell(x - 1, y):
            ++count
        if x + 1 < self.width and self.getCell(x + 1, y):
            ++count
        return count
        


    def step(self):
        boardSize = self.board.shape
        newBoard = np.zeros((boardSize[0], boardSize[1]), dtype=bool)

        for rowInd, row in enumerate(self.board):
            for elInd, element in enumerate(row):
                print(elInd, rowInd, self.countNeighbors(elInd, rowInd))


game = Game(2, 3)
game.setCell(0, 0, True)
game.printBoard()
game.step()

