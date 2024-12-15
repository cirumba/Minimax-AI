import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    max_depth = 5  # Ajuste conforme necessário
    return minimax_move(state, max_depth=max_depth, eval_func=evaluate_count)


def evaluate_count(state, player:str) -> float:
    # Se o estado for terminal, retorne a utilidade do estado
    if state.is_terminal():
        winner = state.winner()
        if winner == player:
            return float('inf')  # Vitória para o jogador atual
        elif winner == state.opponent(player):
            return float('-inf')  # Vitória para o oponente
        else:
            return 0  # Empate

    # Caso não seja terminal, calcule a diferença de peças
    player_count = state.count_pieces(player)
    opponent_count = state.count_pieces(state.opponent(player))
    return player_count - opponent_count
