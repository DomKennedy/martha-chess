# %%
import chess.svg
import chess
from martha_chess.state import GameState, Move
from IPython import display

# %%
def render_state(state: GameState):
    fen = state.to_fen_string()
    return (chess.svg.board(chess.Board(fen), size=350))


# %%
state = GameState()
# %%
# %%

render_state(state)
# %%
