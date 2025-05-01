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


def player(board): #CHECK
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for row in board:
        for tile in row:
            if tile == 'X':
                x += 1
            if tile == 'O':
                o += 1

    if x == 0 and o == 0:
        return 'X'
    if x == o:
        return 'X'
    else:
        return 'O'


def actions(board): #CHECK
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                available.add((i, j))
    return available

def result(board, action): #CHECK
    """
    Returns the board that results from making move (i, j) on the board.
    """
    my_board = copy.deepcopy(board)
    if board[action[0]][action[1]] != EMPTY:
        raise Exception('Illegal movement')
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board): #CHECK
    empty = 0
    for row in board:
        for tile in row:
            if tile == EMPTY:
                empty += 1
    if empty  == 0:
        return True
    else:
        return False
            


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
