
board = [[0 for j in range(8)] for i in range(8)]

def isSafe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < 8:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    if row == 8:
        return True

    for col in range(8):
        if isSafe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


board[0][0] = 1

if solve(1):
    print("Final 8-Queens Matrix:")

    for i in range(8):
        for j in range(8):
            print(board[i][j], end=" ")
        print()
else:
    print("No solution exists.")
