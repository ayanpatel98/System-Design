from PlayerPiece import PlayerPiece
from models.Pieces import Pieces

class PieceO(PlayerPiece):
    def __init__(self):
        super().__init__(Pieces.O)