#include <iostream>
#include <vector>
#include <queue>

void printField(const std::vector< std::string >& field) {
    for (const auto& row: field) {
        std::cout << "|";
        for (size_t i = 0; i < row.length(); ++i) {
            std::cout << row[i] << "|";
        }
        std::cout << std::endl;
    }
}

bool isQueenPlacementPossible(const std::vector<short>& queens, short row, short col) {
    for (short queen_row = 0; queen_row < row; ++queen_row) {
        size_t queen_row_uint = static_cast<size_t>(queen_row);
        if (queens[queen_row_uint] == col || queen_row - row == queens[queen_row_uint] - col || queen_row - row == col - queens[queen_row_uint]) {
            return false;
        }
    }
    return true;
}

bool placeNextQueens(std::vector< std::vector< std::string> >& result, std::vector<short>& queens, short row, short n) {
    if (row == n) {
        return true;
    }
    for (short j = 0; j < n; ++j) {
        // Place a queen if possible
        if (isQueenPlacementPossible(queens, row, j)) {
            queens[row] = j;
            if(placeNextQueens(result, queens, row+1, n)) {
                if (row == n-1) {
                    std::vector<std::string> res{static_cast<size_t>(n), std::string(static_cast<size_t>(n), '.')};
                    for (short i = 0; i < queens.size(); ++i) {
                        res[static_cast<size_t>(i)][static_cast<size_t>(queens[i])] = 'Q';
                    }
                    result.push_back(res);
                }
            }
        }
    }
    return false;
}

std::vector< std::vector<std::string> > solveNQueens(int n) {
    std::vector< std::vector< std::string> > result;

    std::vector<short> queens(n);

    placeNextQueens(result, queens, 0, n);

    return result;
}

int main() {
    std::vector< std::vector<std::string> > result = solveNQueens(9);
    for (const auto& res: result) {
        printField(res);
        std::cout << std::endl;
    }

    return 0;
}
