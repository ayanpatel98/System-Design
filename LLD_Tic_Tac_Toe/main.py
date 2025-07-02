from Player import Player
from Game import Game
from PieceX import PieceX
from PieceO import PieceO

if __name__=="__main__":
    player1 = Player("Ayan", PieceX())
    player2 = Player("XYZ", PieceO())

    game = Game(player1, player2, 3)

    game.startGame()