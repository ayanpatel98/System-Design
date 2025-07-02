from Player import Player
from Board import Board
import collections

class Game:
    def __init__(self, player1: Player, player2: Player, size: int):
        self.playerList = collections.deque([player1, player2])
        self.board = Board(size)
    
    def startGame(self):
        while True:
            player = self.playerList.popleft()

            self.board.printBoard()

            # Check if board is free
            if not self.board.hasFreeCells():
                print("Tie")
                break

            print(player.name, "Enter a row: ")
            r = int(input())
            
            print(player.name, "Enter a column: ")
            c = int(input())

            # Place a piece
            if not self.board.hasPieceAdded(r, c, player.playerPiece):
                self.playerList.appendleft(player)
                print("Please Try again")
                continue
            self.playerList.append(player)
            # check if the player won
            if self.checkIfWon(r, c, player):
                print(player.name, "Won")
                break
    
    def checkIfWon(self, row, col, player: Player):
        n = len(self.board.board)
        streak = 0
        for c in range(n):
            if self.board.board[row][c].piece==player.playerPiece:
                streak+=1
        
        if streak!=n:
            streak = 0
            for r in range(n):
                if self.board.board[r][col].piece==player.playerPiece:
                    streak+=1
        
        if streak!=n:
            streak = 0
            for r in range(n):
                for c in range(n):
                    if r==c and self.board.board[r][c].piece==player.playerPiece:
                        streak+=1
        
        if streak!=n:
            streak = 0
            for r in range(n-1, -1, -1):
                for c in range(n-1, -1, -1):
                    if r==c and self.board.board[r][c].piece==player.playerPiece:
                        streak+=1
                        
        return streak==n
        


        