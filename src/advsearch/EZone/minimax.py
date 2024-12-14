import random
from typing import Tuple, Callable



def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    def maximize(state, alpha, beta, depth, max_depth, eval_func):
        if state.is_terminal() or (max_depth != -1 and depth >= max_depth):
            return eval_func(state, state.player), None

        best_value = float('-inf')
        best_move = None
        
        for move in state.legal_moves():
            successor = state.next_state(move)
            value, _ = minimize(successor, alpha, beta, depth + 1, max_depth, eval_func)
            
            if value > best_value:
                best_value = value
                best_move = move
            
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
                
        return best_value, best_move

    def minimize(state, alpha, beta, depth, max_depth, eval_func):
        if state.is_terminal() or (max_depth != -1 and depth >= max_depth):
            return eval_func(state, state.player), None
            
        best_value = float('inf')
        best_move = None
        
        for move in state.legal_moves():
            
            successor = state.next_state(move)
            value, _ = maximize(successor, alpha, beta, depth + 1, max_depth, eval_func)
            
            if value < best_value:
                best_value = value
                best_move = move
                
            beta = min(beta, best_value)
            if alpha >= beta:
                break
                
        return best_value, best_move

    if state.is_initial_state():
        return (1, 1)  # Best first move for inverted TTT

    value, move = maximize(state, float('-inf'), float('inf'), 0, max_depth, eval_func)
    return move