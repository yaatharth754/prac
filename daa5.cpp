
#include <iostream>
using namespace std;

int board[8][8] = {0};

bool isSafe(int row, int col) {
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1)
            return false;
    }

    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1)
            return false;
    }

    for (int i = row - 1, j = col + 1; i >= 0 && j < 8; i--, j++) {
        if (board[i][j] == 1)
            return false;
    }

    return true;
}

bool solve(int row) {
    if (row == 8)
        return true;

    for (int col = 0; col < 8; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;

            if (solve(row + 1))
                return true;

            board[row][col] = 0;
        }
    }

    return false;
}

int main() {
    // Place the first queen at row 0, column 0
    board[0][0] = 1;

    if (solve(1)) {
        cout << "Final 8-Queens Matrix:\n";

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++)
                cout << board[i][j] << " ";
            cout << endl;
        }
    } else {
        cout << "No solution exists.\n";
    }

    return 0;
}
