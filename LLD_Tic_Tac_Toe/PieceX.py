from PlayerPiece import PlayerPiece
from models.Pieces import Pieces

class PieceX(PlayerPiece):
    def __init__(self):
        super().__init__(Pieces.X)