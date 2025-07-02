from PlayerPiece import PlayerPiece

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board= [[PlayerPiece() for j in range(self.size)] for i in range(self.size)]
    
    def hasPieceAdded(self, r, c, playerPiece: PlayerPiece):
        if r<0 or r>=self.size or c<0 or c>=self.size:
            return False
        
        if self.board[r][c].piece==None:
            self.board[r][c].piece = playerPiece.piece
            return True
        return False
    
    def hasFreeCells(self):
        n = len(self.board)

        for r in range(n):
            for c in range(n):
                if self.board[r][c].piece==None:
                    return True
        return False
    

    def printBoard(self):
        n = self.size
        for r in range(n):
            rowList = []
            for c in range(n):
                rowList.append(self.board[r][c].piece)
            print(rowList)