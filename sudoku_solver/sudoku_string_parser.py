from sudoku_solver.sudoku_solver import Sudoku, Row, Cell

def parse_sudoku_from_string(string_sudoku: str) -> "Sudoku":
    sudoku = Sudoku()
    string_sudoku_stripped = string_sudoku.strip().strip("\n")
    lines = string_sudoku_stripped.splitlines()
    row_number = 0
    for idx, line in enumerate(lines):
        if idx in [3, 7]:
            continue
        parse_sudoku_row_string(sudoku, line, row_number)
        row_number += 1
    return sudoku

def parse_sudoku_row_string(sudoku: Sudoku, string_sudoku_row: str, row_number: int) -> Row:
    number_indices = [0, 2, 4, 8, 10, 12, 16, 18, 20]
    for idx, index in enumerate(number_indices):
        number = string_sudoku_row[index]
        value = int(number) if number != " " else 0
        cell = Cell(value)
        sudoku.rows[row_number].cells.append(cell)
        sudoku.columns[idx].cells.append(cell)