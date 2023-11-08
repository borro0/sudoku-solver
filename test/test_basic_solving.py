import pytest
from sudoku_solver.sudoku_solver import solve_sudoku
from sudoku_solver.sudoku_solver import Sudoku


def test_FromAndToStringCompleteSolution():
    sudoku_string_input = (
        "5 1 7 | 6 8 9 | 4 3 2\n"
        "3 8 6 | 1 2 4 | 5 9 7\n"
        "4 9 2 | 5 7 3 | 1 8 6\n"
        "---------------------\n"
        "7 5 4 | 9 3 2 | 8 6 1\n"
        "1 2 9 | 4 6 8 | 3 7 5\n"
        "8 6 3 | 7 1 5 | 9 2 4\n"
        "---------------------\n"
        "6 4 8 | 2 9 1 | 7 5 3\n"
        "9 7 5 | 3 4 6 | 2 1 8\n"
        "2 3 1 | 8 5 7 | 6 4 9\n"
    )
    sudoku = Sudoku.from_string(sudoku_string_input)
    sudoku_string_output = sudoku.to_string()
    assert sudoku_string_output == sudoku_string_input


def test_FromAndToStringInCompleteSolution():
    sudoku_string_input = (
        "5 1 7 | 6 8   | 4 3 2\n"
        "3 8 6 | 1 2 4 | 5 9 7\n"
        "4 9 2 | 5 7 3 | 1 8 6\n"
        "---------------------\n"
        "7 5 4 | 9 3 2 | 8 6 1\n"
        "1 2 9 | 4   8 | 3 7  \n"
        "8 6 3 | 7 1 5 | 9 2 4\n"
        "---------------------\n"
        "  4 8 | 2 9 1 | 7 5 3\n"
        "9 7 5 |   4 6 | 2 1 8\n"
        "2 3 1 | 8 5 7 | 6 4 9\n"
    )
    sudoku = Sudoku.from_string(sudoku_string_input)
    sudoku_string_output = sudoku.to_string()
    assert sudoku_string_output == sudoku_string_input
