class GameState:
    def __init__(self):
        # TODO: implement
        pass

    def move(self, move: "Move") -> "GameState":
        # TODO: implement
        pass

    def to_fen_string(self) -> str:
        """Translate this game state into Forsyth-Edwards Notation, which can be
        parsed by various off-the-shelf chess rendering tools"""

        # TODO: update this function so it actually returns the FEN representation
        # of self, rather than just always returning the starting position
        return "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# TODO: implement
class Move:
    pass