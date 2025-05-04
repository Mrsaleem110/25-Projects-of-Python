# Sample Sudoku board (0 means empty cell)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to print the board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(bo[i][j] if bo[i][j] != 0 else ".", end=" ")
        print()

# Function to find empty cell
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

# Check if move is valid
def is_valid(bo, num, pos):
    row, col = pos

    # Row check
    if num in bo[row]:
        return False

    # Column check
    if num in [bo[i][col] for i in range(9)]:
        return False

    # Box check
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num:
                return False

    return True

# Backtracking Solver
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True  # Solved!
    row, col = find

    for num in range(1, 10):
        if is_valid(bo, num, (row, col)):
            bo[row][col] = num
            if solve(bo):
                return True
            bo[row][col] = 0  # Backtrack

    return False

# Running the solver
print("Original Board:")
print_board(board)
solve(board)
print("\nSolved Board:")
print_board(board)
