import pytest
from sudoku_solver.sudoku_solver import solve_sudoku


def test_GivenCompletedSolution():
    sudoku_input = """
    5 1 7 | 6 8 9 | 4 3 2
    3 8 6 | 1 2 4 | 5 9 7
    4 9 2 | 5 7 3 | 1 8 6
    ---------------------
    7 5 4 | 9 3 2 | 8 6 1
    1 2 9 | 4 6 8 | 3 7 5
    8 6 3 | 7 1 5 | 9 2 4
    ---------------------
    6 4 8 | 2 9 1 | 7 5 3
    9 7 5 | 3 4 6 | 2 1 8
    2 3 1 | 8 5 7 | 6 4 9
    """
    result = solve_sudoku(sudoku_input)
    assert result == sudoku_input
