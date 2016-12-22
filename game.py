import numpy as np

class Game:

    def printBoard(self):
        print("\n")
        for row in self.board:
            for element in row:
                if element:
                    print("1 ", end="")
                else:
                    print("- ", end="")
            print("\n")

   
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=bool)
        #self.printBoard()

    def setCell(self, x, y, val):
        self.board[y, x] = val

    def getCell(self, x, y):
        return self.board[y, x]

    def setCellBoard(self, x, y, val, board):
        board[y, x] = val

    
    def countNeighbors(self, x, y):
        #print("cell", x, y)
        count = 0;
        if y - 1 >= 0:
            #print("y-1", y - 1)
            count += self.checkThreeRow(x, y - 1)
        if y + 1 < self.height:
            #print("y+1", y+1)
            count += self.checkThreeRow(x, y + 1)

        if x - 1 >= 0 and self.getCell(x - 1, y):
            #print("x-1", x-1)
            count += 1
        if x + 1 < self.width and self.getCell(x + 1, y):
            #print("x+1", x+1)
            count += 1

        return count
                
    def checkThreeRow(self, x, y):
        count = 0
        if self.getCell(x, y):
            count += 1
        if x - 1 >= 0 and self.getCell(x - 1, y):
            count += 1
        if x + 1 < self.width and self.getCell(x + 1, y):
            count += 1
        return count
        
    def getCellBoard(self, x, y, board):
        return board[y, x]


    def step(self):
        boardSize = self.board.shape
        newBoard = np.zeros((boardSize[0], boardSize[1]), dtype=bool)

        for rowInd, row in enumerate(self.board):
            for elInd, element in enumerate(row):
                #print(elInd, rowInd, self.countNeighbors(elInd, rowInd))
                neighbors = self.countNeighbors(elInd, rowInd) 
                if neighbors < 2:
                    self.setCellBoard(elInd, rowInd, False, newBoard)
                elif neighbors == 2 or neighbors == 3:
                    self.setCellBoard(elInd, rowInd, True, newBoard)
                elif neighbors > 3:
                    self.setCellBoard(elInd, rowInd, False, newBoard)
                elif self.getCellBoard(elInd, rowInd, newBoard) == False and neighbors == 3:
                    self.setCellBoard(elInd, rowInd, True, newBoard)

        self.board = newBoard



game = Game(30, 30)
game.setCell(15, 15, True)
game.setCell(16, 16, True)
game.setCell(15, 16, True)
game.setCell(15, 17, True)
game.printBoard()
#print("height", game.height, "width", game.width)
game.step()
game.printBoard()
