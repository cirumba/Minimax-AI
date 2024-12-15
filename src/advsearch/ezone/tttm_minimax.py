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
    """
    Retorna uma jogada calculada pelo algoritmo Minimax com poda Alpha-Beta.
    """
    return minimax_move(state, max_depth=9, eval_func=utility)

def utility(state: GameState, player: str) -> float:
    """
    Retorna a utilidade de um estado (terminal) para o jogador especificado.
    :param state: O estado de jogo atual.
    :param player: O jogador para quem estamos calculando a utilidade ('B' ou 'W').
    :return: Valor positivo se o jogador venceu, negativo se perdeu, e 0 para empate.
    """
    winner = state.winner()

    if winner is None:
        return heuristic_score(state, player)  # Empate ou estado não terminal.

    # No Misere, vencer o jogo tradicional significa perder.
    # O valor é negativo se o jogador atual ganha no sentido tradicional.
    return 100 if winner == player else -100

def heuristic_score(state: GameState, player: str) -> float:
    # Pesos estratégicos
    strategic_weights = {
        (1, 1): 3,  # Centro
        (0, 0): 2, (0, 2): 2, (2, 0): 2, (2, 2): 2,  # Cantos
        (0, 1): 1, (1, 0): 1, (1, 2): 1, (2, 1): 1   # Laterais
    }

    opponent = 'B' if player == 'W' else 'W'  # Identificar oponente
    score = 0

    for x, y in state.legal_moves():
        if (x, y) in strategic_weights:
            score += strategic_weights[(x, y)]  # Posições estratégicas
        # Verificar se a jogada leva à vitória do jogador
        next_state = state.next_state((x, y))
        if next_state.is_winner(player):  # Vitória imediata
            return 1000
        # Penalizar se a jogada permite vitória do adversário
        elif next_state.is_winner(opponent):
            score -= 500  # Penalidade alta para evitar derrotas
    return score

