import copy

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'O'
            eval = minimax(board_copy, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'X'
            eval = minimax(board_copy, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_score = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board_copy = copy.deepcopy(board)
        board_copy[i][j] = 'O'
        score = minimax(board_copy, 0, False)
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Cell already occupied. Try again.")
            continue

       
        if is_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break

        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        
        print("AI's turn:")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = 'O'

        
        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins! Better luck next time.")
            break

        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
