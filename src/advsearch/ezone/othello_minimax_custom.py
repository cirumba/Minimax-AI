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
EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]


def make_move(state) -> Tuple[int, int]:
    max_depth = 5  # Ajuste conforme o limite de tempo
    return minimax_move(state, max_depth=max_depth, eval_func=evaluate_custom)

def evaluate_custom(state, player: str) -> float:
    opponent = 'B' if player == 'W' else 'W'
    positional_score = 0
    mobility_score = 0
    corner_score = 0

    # Verificar se o estado é terminal
    if state.board.is_terminal_state():
        winner = state.board.winner()
        if winner == player:
            return float('inf')  # Vitória para o jogador atual
        elif winner == opponent:
            return float('-inf')  # Vitória para o oponente
        else:
            return 0

    # Pontuação posicional usando a máscara EVAL_TEMPLATE
    for y in range(8):
        for x in range(8):
            piece = state.board.tiles[y][x]
            if piece == player:
                positional_score += EVAL_TEMPLATE[y][x]
            elif piece == opponent:
                positional_score -= EVAL_TEMPLATE[y][x]

    # Mobilidade ajustada
    player_moves = len(state.board.legal_moves(player))
    opponent_moves = len(state.board.legal_moves(opponent))
    total_moves = player_moves + opponent_moves
    if total_moves > 0:
        mobility_score = 100 * (player_moves - opponent_moves) / total_moves

    # Controle de cantos com peso ajustado
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    for x, y in corners:
        piece = state.board.tiles[y][x]
        if piece == player:
            corner_score += 25  # Peso maior para cantos
        elif piece == opponent:
            corner_score -= 25

    # Combinação das pontuações ponderadas
    return (
        1.0 * positional_score +
        0.5 * mobility_score +
        0.9 * corner_score
    )