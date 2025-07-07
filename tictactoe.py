def draw_board(board_state):
    print(board_state[6] + '|' + board_state[7] + '|' + board_state[8])
    print('-+-+-')
    print(board_state[3] + '|' + board_state[4] + '|' + board_state[5])
    print('-+-+-')
    print(board_state[0] + '|' + board_state[1] + '|' + board_state[2])

def get_empty_cells(board_state):
    return [i for i in range(9) if board_state[i] == ' ']

def is_winning(board_state):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]              
    ]
    for a, b, c in win_conditions:
        if board_state[a] == board_state[b] == board_state[c] and board_state[a] != ' ':
            return True
    return False

def minimax(board_state, is_maximizing):
    if is_winning(board_state):
        return 1 if not is_maximizing else -1
    if not get_empty_cells(board_state):
        return 0  

    symbol = 'O' if is_maximizing else 'X'
    best_score = float('-inf') if is_maximizing else float('inf')

    for i in get_empty_cells(board_state):
        board_state[i] = symbol
        score = minimax(board_state, not is_maximizing)
        board_state[i] = ' '
        best_score = max(best_score, score) if is_maximizing else min(best_score, score)

    return best_score

def computer_move(board_state):
    best_score = float('-inf')
    move = None
    for i in get_empty_cells(board_state):
        board_state[i] = 'O'
        score = minimax(board_state, False)
        board_state[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    board_state[move] = 'O'

def human_move(board_state):
    best_score = float('-inf')
    move = None
    for i in get_empty_cells(board_state):
        board_state[i] = 'X'
        score = minimax(board_state, True)
        board_state[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    board_state[move] = 'X'

def play_auto_game(verbose=True):
    board_state = [' '] * 9
    turn = 'X'
    while True:
        if turn == 'X':
            human_move(board_state)
        else:
            computer_move(board_state)

        if verbose:
            draw_board(board_state)
            print()

        if is_winning(board_state):
            print(f"{turn} wins!")
            return turn
        elif not get_empty_cells(board_state):
            print("It's a draw!")
            return "Draw"
        turn = 'O' if turn == 'X' else 'X'


for i in range(5):
    print(f"--- Game {i+1} ---")
    result = play_auto_game(verbose=True)
    print(f"Result: {result}\n")
