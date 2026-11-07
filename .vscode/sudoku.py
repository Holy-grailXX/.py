def find_empty(board):
    """Step 1: scan for the first empty cell."""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def is_valid(board, row, col, num):
    """Constrain: num must not already be in the row, column, or 3x3 box."""
    
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    
    box_r, box_c = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if board[r][c] == num:
                return False

    return True


def solve_sudoku(board):
    empty = find_empty(board)

    
    if empty is None:
        return True

    row, col = empty

    
    for num in range(1, 10):
        if is_valid(board, row, col, num):   
            board[row][col] = num           
            if solve_sudoku(board):         
                return True
            board[row][col] = 0              
    
    return False



board = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],
    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],
    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9],
]

if solve_sudoku(board):
    for row in board:
        print(row)
else:
    print("No solution exists")