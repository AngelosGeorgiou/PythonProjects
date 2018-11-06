# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all
# cells of the grid with digits from 1 to 9, so that each column, each row,
# and each of the nine 3x3 sub-grids (also known as blocks) contain all of the
# digits from 1 to 9. (More info at: http://en.wikipedia.org/wiki/Sudoku)
# Sudoku Solution Validator 
# Write a function
# validSolution/ValidateSolution/valid_solution() that accepts a 2D array
# representing a Sudoku board, and returns true if it is a valid solution, or
# false otherwise. The cells of the sudoku board may also contain 0's, which
# will represent empty cells. Boards containing one or more zeroes are
# considered to be invalid solutions.

def validSolution(board):
    for i in range(0,9):
        a = list(range(10))
        b = list(range(10))
        for j in range(0,9):
            if board[i][j] in a: a.remove(board[i][j])
            else: return False
            if board[j][i] in b: b.remove(board[j][i])
            else: return False
    for x in [0,3,6]:
        for y in [0,3,6]:
            a = list(range(10))
            for i in range(0,3):
                for j in range(0,3):
                    if board[x+j][y+i] in a: a.remove(board[x+j][y+i])
                    else: return False              
    return True