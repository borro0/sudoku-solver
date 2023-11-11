import pytest
from sudoku_solver.sudoku_string_parser import parse_sudoku_from_string

@pytest.fixture
def completed_sudoku_string():
    return (
        "5 1 7 | 6 8 9 | 4 3 2 \n"
        "3 8 6 | 1 2 4 | 5 9 7 \n"
        "4 9 2 | 5 7 3 | 1 8 6 \n"
        "--------------------- \n"
        "7 5 4 | 9 3 2 | 8 6 1 \n"
        "1 2 9 | 4 6 8 | 3 7 5 \n"
        "8 6 3 | 7 1 5 | 9 2 4 \n"
        "--------------------- \n"
        "6 4 8 | 2 9 1 | 7 5 3 \n"
        "9 7 5 | 3 4 6 | 2 1 8 \n"
        "2 3 1 | 8 5 7 | 6 4 9 \n"
    )


def test_FromAndToStringCompleteSolution(completed_sudoku_string):
    sudoku = parse_sudoku_from_string(completed_sudoku_string)
    sudoku_string_output = sudoku.to_string()
    assert sudoku_string_output == completed_sudoku_string


def test_FromAndToStringInCompleteSolution():
    sudoku_string_input = (
        "5 1 7 | 6 8   | 4 3 2 \n"
        "3 8 6 | 1 2 4 | 5 9 7 \n"
        "4 9 2 | 5 7 3 | 1 8 6 \n"
        "--------------------- \n"
        "7 5 4 | 9 3 2 | 8 6 1 \n"
        "1 2 9 | 4   8 | 3 7   \n"
        "8 6 3 | 7 1 5 | 9 2 4 \n"
        "--------------------- \n"
        "  4 8 | 2 9 1 | 7 5 3 \n"
        "9 7 5 |   4 6 | 2 1 8 \n"
        "2 3 1 | 8 5 7 | 6 4 9 \n"
    )
    sudoku = parse_sudoku_from_string(sudoku_string_input)
    sudoku_string_output = sudoku.to_string()
    assert sudoku_string_output == sudoku_string_input


# def test_ColumnsParsedCorrectly(completed_sudoku_string):
#     columns = [
#         [5, 3, 4, 7, 1, 8, 6, 9, 2],
#         [1, 8, 9, 5, 2, 6, 4, 7, 3],
#         [7, 6, 2, 4, 9, 3, 8, 5, 1],
#         [6, 1, 5, 9, 4, 7, 2, 3, 8],
#         [8, 2, 7, 3, 6, 1, 9, 4, 5],
#         [9, 4, 3, 2, 8, 5, 1, 6, 7],
#         [4, 5, 1, 8, 3, 9, 7, 2, 6],
#         [3, 9, 8, 6, 7, 2, 5, 1, 4],
#         [2, 7, 6, 1, 5, 4, 3, 8, 9],
#     ]
#     sudoku = parse_sudoku_from_string(completed_sudoku_string)
#     assert len(sudoku.columns) == 9
#     for column in sudoku.columns:
#         assert len(column.cells) == 9
#         for idx, cell in enumerate(column.cells):
#             assert cell.value == column[idx]