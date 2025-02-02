from typing import List, Set

def main():
    print("Hello, World!")
    print(get_fibonacci(6))

    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solve_sudoku(board)
    print_board(board)

# Solve Sudoku inplace in board
def solve_sudoku(board: List[List[str]]) -> None:
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]

    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem != '.':
                rows[i].add(elem)
                columns[j].add(elem)
                square_index = (i // 3) * 3 + (j // 3)
                squares[square_index].add(elem)

    place_next_number(board, 0, 0, rows, columns, squares)

def place_next_number(
    board: List[List[str]],
    row: int,
    col: int,
    rows: List[Set[str]],
    columns: List[Set[str]],
    squares: List[Set[str]]
) -> bool:
    if col == 9:
        col = 0
        row += 1
        if row == 9:
            return True

    if board[row][col] == '.':
        for digit in range(1, 10):
            str_digit = str(digit)
            if can_place(str_digit, row, col, rows, columns, squares):
                place_number(board, str_digit, row, col, rows, columns, squares)
                if place_next_number(board, row, col + 1, rows, columns, squares):
                    return True
                remove_number(board, str_digit, row, col, rows, columns, squares)
    else:
        return place_next_number(board, row, col + 1, rows, columns, squares)
    return False

def can_place(
    digit: str, row: int, col: int, rows: List[Set[str]],
    columns: List[Set[str]], squares: List[Set[str]]
) -> bool:
    return digit not in rows[row] and digit not in columns[col] and digit not in squares[(row // 3) * 3 + col // 3]

def place_number(
    board: List[List[str]], digit: str, row: int, col: int, rows: List[Set[str]],
    columns: List[Set[str]], squares: List[Set[str]]
) -> None:
    rows[row].add(digit)
    columns[col].add(digit)
    squares[(row // 3) * 3 + col // 3].add(digit)
    board[row][col] = digit

def remove_number(
    board: List[List[str]], digit: str, row: int, col: int, rows: List[Set[str]],
    columns: List[Set[str]], squares: List[Set[str]]
) -> None:
    board[row][col] = '.'
    rows[row].remove(digit)
    columns[col].remove(digit)
    squares[(row // 3) * 3 + col // 3].remove(digit)

def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(row)

def get_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    main()
