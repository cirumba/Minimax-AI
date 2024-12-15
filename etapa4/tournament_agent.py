import random
from typing import Tuple

from advsearch.ezone.minimax import minimax_move
from ..othello.gamestate import GameState
from ..othello.board import Board

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.
def make_move(state) -> Tuple[int, int]:
    max_depth = 3  # Ajuste conforme o limite de tempo
    return minimax_move(state, max_depth=max_depth, eval_func=evaluate_custom)

def evaluate_custom(state, player):
    """
    Nova heurística customizada simples para Othello.
    :param state: Estado atual do jogo.
    :param player: Jogador atual (preto ou branco).
    :return: Avaliação do estado (score).
    """
    opponent = Board.opponent(player)
    board = state.get_board()

    # Mobilidade: diferença entre jogadas legais do jogador e do oponente
    player_moves = len(board.legal_moves(player))
    opponent_moves = len(board.legal_moves(opponent))
    mobility_score = player_moves - opponent_moves

    # Controle de Bordas: conte peças do jogador nas bordas
    edges = [
        board.tiles[0],       # Linha superior
        board.tiles[-1],      # Linha inferior
        [row[0] for row in board.tiles],  # Coluna esquerda
        [row[-1] for row in board.tiles]  # Coluna direita
    ]
    edge_control = sum(edge.count(player) - edge.count(opponent) for edge in edges)

    # Pesos ajustáveis
    mobility_weight = 0.7
    edge_control_weight = 0.3

    # Score final
    return mobility_weight * mobility_score + edge_control_weight * edge_control


