import random
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    print(f"Current State: {state}")
    move = minimax_move(state, 9, utility)
    print(f"Chosen Move: {move}")

def utility(state, player:str) -> float:
    winner = state.winner()
    if winner == player:
        return 1  
    elif winner is not None:
        return -1
    elif state.is_terminal():
        return 0
    return 0
