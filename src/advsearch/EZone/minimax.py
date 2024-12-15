import random
from typing import Tuple, Callable
import math
from ..tttm.gamestate import GameState



def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    if state.is_initial_state():
        return (1, 1)
    
    def minimax(state: GameState, depth: int, alpha: float, beta: float, maximizing_player: bool) -> Tuple[float, Tuple[int, int]]:
       
        if state.is_terminal() or (depth == 0 and max_depth != -1):
            score = eval_func(state, state.player)
            print(f"Terminal State: {state}\nScore: {score}\n")
            return score, None

        best_move = None

        if maximizing_player:
            max_eval = -math.inf
            for action in state.legal_moves():
                successor = state.next_state(action)
                eval_score, _ = minimax(successor, depth - 1, alpha, beta, False)
                #print(f"Maximizing: Action: {action}, Eval: {eval_score}")
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = action
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Poda
            return max_eval, best_move
        else:
            min_eval = math.inf
            for action in state.legal_moves():
                successor = state.next_state(action)
                eval_score, _ = minimax(successor, depth - 1, alpha, beta, True)
                #print(f"Minimizing: Action: {action}, Eval: {eval_score}")
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = action
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Poda
            return min_eval, best_move

    _, best_move = minimax(state, max_depth, -math.inf, math.inf, state.player == 'B')
    print(f"Chosen Move: {best_move}")
    return best_move