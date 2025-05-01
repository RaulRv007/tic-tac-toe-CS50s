from tictactoe import player, actions, result, terminal
X = "X"
O = "O"
EMPTY = None
board = [[X, X, O],
         [O, X, O],
         [X, O, X]]
print(player(board))
print(actions(board))
#sprint(result(board, (0, 1)))
print(terminal(board))
