"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    total_x = 0
    total_o = 0

    if not X or O in board:
        return X
    else:
        for row in board:
            for cel in row:
                if cel == X:
                    total_x += 1
                if cel == O:
                    total_o += 1
    
    if total_x > total_o:
        return O
    else: 
        return X    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible_actions = set()

    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            if board[r][c] == EMPTY:
                possible_actions.add((r, c))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copied_board = copy.deepcopy(board)
    player_turn = player(copied_board)
    copied_board[action[0]][action[1]] = player_turn

    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    winner = None

    #If all the celds in a row are the same player
    if all(i == board[0][0] for i in board[0]):
        if board[0][0] is not None:
            return board[0][0]
        winner = board[0][0]
    if all(i == board[1][0] for i in board[1]):
        if board[1][0] is not None:
            return board[1][0]
        winner = board[1][0]
    if all(i == board[2][0] for i in board[2]):
        if board[2][0] is not None:
            return board[2][0]
        winner = board[2][0]

    #If all the celds in a column are the same player
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        winner = board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        winner = board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        winner = board[0][2]

    #If all the celds in a diagonal are the same player
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        winner = board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        winner = board[0][2]

    #Game finish in tie
    else: 
        winner = None

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in row for row in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    value = float('-inf')
    move = None

    for action in actions(board):
        maxim, actual = min_value(result(board, action))
        if maxim > value:
            value = maxim
            move = action
            if value == 1:
                return value, move

    return value, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    value = float('inf')
    move = None

    for action in actions(board):
        minim, actual = max_value(result(board, action))
        if minim < value:
            value = minim
            move = action
            if value == -1:
                return value, move

    return value, move