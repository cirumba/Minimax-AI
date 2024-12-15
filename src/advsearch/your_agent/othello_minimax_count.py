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
    
    if state.board.is_terminal_state():
        winner = state.board.winner()
        if winner == player:
            return 31  # Vitória para o jogador atual
        elif winner is None:
            return 0  # Empate
        else:
            return -31  # Vitória para o oponente
        
    opponent = Board.opponent(player)
    # Contar peças diretamente no tabuleiro
    player_count = state.board.num_pieces(player)
    opponent_count = state.board.num_pieces(opponent)

    return player_count - opponent_count
