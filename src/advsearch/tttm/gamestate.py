from typing import Tuple, Union
from .board import Board

class GameState:

    game_name = "Tic-Tac-Toe Misere"

    def __str__(self):
        """
        Retorna uma representação legível do estado do jogo, incluindo o tabuleiro e o jogador atual.
        """
        board_str = str(self.board)  # Assume que Board já implementa __str__
        return f"Player: {self.player}\nBoard:\n{board_str}"

    def __init__(self, board: Board, player: str):
        self.board = board
        self.player = player

    def is_initial_state(self) -> bool:
        return all(self.board.is_empty(row, col) for row in range(3) for col in range(3))

    def is_terminal(self) -> bool:
        return self.board.is_full() or self.winner() is not None

    def is_legal_move(self, move: Tuple[int, int]) -> bool:
        col, row = move
        return 0 <= row < 3 and 0 <= col < 3 and self.board.is_empty(row, col)

    def legal_moves(self) -> list:
        return [(col, row) for row in range(3) for col in range(3) if self.is_legal_move((col, row))]

    def winner(self) -> Union[str, None]:
        loser = self.board.check_loser()
        if loser == 'B':
            return 'W'
        elif loser == 'W':
            return 'B'
        else:
            return None

    def get_board(self) -> Board:
        return self.board

    def copy(self) -> 'GameState':
        new_state = GameState(self.board.copy(), self.player)
        return new_state

    def next_state(self, move: Tuple[int, int]) -> 'GameState':
        if not self.is_legal_move(move):
            raise ValueError("Invalid move.")
        
        new_state = self.copy()
        col, row = move
        new_state.board.place_marker(self.player, row, col)

        # Toggle the player for the next move
        new_state.player = 'B' if self.player == 'W' else 'W'

        return new_state
