import random
from typing import Tuple, Callable



def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    def minimax(state, depth, alpha, beta, maximizing):
        if state.is_terminal():
            return eval_func(state, state.player), None  # Avalie diretamente

        legal_moves = state.legal_moves()
        best_move = None

        if maximizing:
            value = float('-inf')
            for move in legal_moves:
                next_state = state.next_state(move)
                eval_score, _ = minimax(next_state, depth + 1, alpha, beta, False)
                if eval_score > value:
                    value = eval_score
                    best_move = move  # Remover o espelhamento
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value, best_move
        else:
            value = float('inf')
            for move in legal_moves:
                next_state = state.next_state(move)
                eval_score, _ = minimax(next_state, depth + 1, alpha, beta, True)
                if eval_score < value:
                    value = eval_score
                    best_move = move  # Remover o espelhamento
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value, best_move

    if len(state.legal_moves()) == 9:
        return (1, 1)  # Centralize na primeira jogada

    _, move = minimax(state, 0, float('-inf'), float('inf'), True)
    return move