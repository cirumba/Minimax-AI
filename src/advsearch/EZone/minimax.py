import random
from typing import Tuple, Callable



def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
        def minimax(state, depth, maximizing_player):
            if depth == 0 or state.is_terminal():
                return eval_func(state, state.player), None

            legal_moves = state.legal_moves()
            if maximizing_player:
                max_eval = float('-inf')
                best_move = None
                for move in legal_moves:
                    new_state = state.next_state(move)
                    eval_score, _ = minimax(new_state, depth - 1, False)
                    if eval_score > max_eval:
                        max_eval = eval_score
                        best_move = move
                return max_eval, best_move
            else:
                min_eval = float('inf')
                best_move = None
                for move in legal_moves:
                    new_state = state.next_state(move)
                    eval_score, _ = minimax(new_state, depth - 1, True)
                    if eval_score < min_eval:
                        min_eval = eval_score
                        best_move = move
                return min_eval, best_move

        _, best_move = minimax(state, max_depth, True)
        return best_move