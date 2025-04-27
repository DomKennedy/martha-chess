from martha_chess.state import GameState

def test_to_fen_string():
    state = GameState()
    result = state.to_fen_string()
    expected_result = (
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    )
    assert result == expected_result