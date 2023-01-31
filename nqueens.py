import sys


def _get_arg(argv):
    """
    Get argument if it is valid or exits the program
    """
    # Wrong number of arguments
    if len(argv) != 2:
        print("Usage: nqueens N")
    # N must be an integer greater or equal to 4
    else:
        if argv[1].isdigit():
            number = int(argv[1])
            if number > 3:
                return number
            else:
                print("N must be at least 4")
        else:
            print("N must be a number")
    sys.exit(1)


def _build_chessboard():
    """
    Builds the chessboard taking N to create the dimension.
    """
    return [[" " for i in range(n)] for j in range(n)]


def _print_solution():
    """
    Given a solution it is printed accordingly to the format [[column, row],[column, row],[column, row],[column, row]]
    indicating where are the queens.
    """
    solution = []
    for i in range(n):
        solution.append([i, chessboard[i].index("X")])
    print(solution)


def _is_safe_same_upper_col(row, col):
    """
    Check if there is any queen for same upper column
    """
    while row >= 0:
        if chessboard[row][col] == "X":
            return False
        else:
            row -= 1
    return True


def _is_safe_upper_right_diagonal(row, col):
    """
    Check if there is any queen for upper right diagonal
    """
    while col < n and row >= 0:
        if chessboard[row][col] == "X":
            return False
        else:
            col += 1
            row -= 1
    return True


def _is_safe_upper_left_diagonal(row, col):
    """
    Check if there is any queen for upper left diagonal
    """
    while col >= 0 and row >= 0:
        if chessboard[row][col] == "X":
            return False
        else:
            row -= 1
            col -= 1
    return True


def _is_safe(row, col):
    """
    Check if there is safe to locate a queen in a specific cell
    """
    if _is_safe_same_upper_col(row, col) is False:
        return False
    if _is_safe_upper_right_diagonal(row, col) is False:
        return False
    if _is_safe_upper_left_diagonal(row, col) is False:
        return False
    return True


def _solve_n_queens(row):
    """
    Main function to solve n queens.

    Queen is depicted by "X". The strategy solves 1 case and rest recursion will follow. For each position, it checks if
    it is safe and if it is safe it makes a recursive call with row+1, chessboard[i][j]='X' and then revert the change
    in the chessboard that is make the chessboard[i][j]=' ' again to generate more solutions
    """
    if row == n:
        _print_solution()
        return

    for col in range(n):
        if _is_safe(row, col):
            chessboard[row][col] = "X"
            _solve_n_queens(row + 1)
            chessboard[row][col] = " "


n = _get_arg(sys.argv)
chessboard = _build_chessboard()
_solve_n_queens(0)
