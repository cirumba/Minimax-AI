from advsearch.ezone.othello_minimax_count import evaluate_count
from advsearch.ezone.othello_minimax_mask import evaluate_mask
from advsearch.ezone.othello_minimax_custom import evaluate_custom
from advsearch.othello.board import Board
from advsearch.othello.gamestate import GameState
from advsearch.ezone.minimax import minimax_move 


def play_game(heuristic1, heuristic2, max_depth=3):
    """
    Executa uma partida entre dois jogadores usando minimax com diferentes heurísticas.
    Imprime os movimentos e o estado do tabuleiro no terminal.
    :param heuristic1: Função de avaliação para o primeiro jogador.
    :param heuristic2: Função de avaliação para o segundo jogador.
    :param max_depth: Profundidade máxima do Minimax.
    :return: Vencedor, contagem de peças do Preto, contagem de peças do Branco.
    """
    board = Board()
    state = GameState(board, Board.BLACK)  # Preto começa

    # Configuração inicial de jogadores
    players = {
        Board.BLACK: heuristic1,  # Jogador Preto usa a primeira heurística
        Board.WHITE: heuristic2   # Jogador Branco usa a segunda heurística
    }

    round_num = 1
    while not state.is_terminal():
        current_player = state.player
        print(f"Rodada {round_num}: Jogador {'Preto' if current_player == Board.BLACK else 'Branco'}")

        # Calcular o melhor movimento usando Minimax
        move = minimax_move(state, max_depth=max_depth, eval_func=players[current_player])
        print(f"Melhor movimento: {move}")

        # Atualizar o estado do jogo
        state = state.next_state(move)

        # Imprimir o estado do tabuleiro
        print("Tabuleiro atualizado:")
        state.board.print_board()
        print("-" * 40)

        round_num += 1

    # Resultados finais
    black_count = state.board.num_pieces(Board.BLACK)
    white_count = state.board.num_pieces(Board.WHITE)
    winner = state.winner()

    print("Fim da partida!")
    print(f"Vencedor: {'Preto' if winner == Board.BLACK else 'Branco' if winner == Board.WHITE else 'Empate'}")
    print(f"Placar Final: Preto {black_count} - Branco {white_count}")
    return winner, black_count, white_count


# Executar partida Contagem de Peças X Valor Posicional
winner, black_count, white_count = play_game(evaluate_mask, evaluate_custom)

# Exibir resultado final
print("Partida: Contagem de Peças (Preto) X Valor Posicional (Branco)")
print(f"Vencedor: {'Preto' if winner == Board.BLACK else 'Branco' if winner == Board.WHITE else 'Empate'}")
print(f"Placar Final: Preto {black_count} - Branco {white_count}")