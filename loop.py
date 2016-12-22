from game import Game
from time import sleep

"""
game = Game(30, 30)
game.printBoard()
#print("height", game.height, "width", game.width)
game.step()
game.printBoard()
game.step()
game.printBoard()
"""
def loop(game):
    print(chr(27) + "[2J")
    game.step()
    game.printBoard()


def main():
    width = 30
    height = 30

    game = Game(width, height)

    game.setCell(15, 15, True)
    game.setCell(16, 16, True)
    game.setCell(15, 16, True)
    game.setCell(15, 17, True)

    while True:
        #print("test")
        loop(game)
        sleep(1)

    
main()

