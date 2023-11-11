from sudoku_solver.sudoku_solver import Sudoku, Row

def parse_sudoku_from_string(string_sudoku: str) -> "Sudoku":
    sudoku = Sudoku()
    string_sudoku_stripped = string_sudoku.strip().strip("\n")
    lines = string_sudoku_stripped.splitlines()
    for idx, line in enumerate(lines):
        if idx in [3, 7]:
            continue
        row = parse_sudoku_row_string(line)
        sudoku.rows.append(row)
    return sudoku

def parse_sudoku_row_string(string_sudoku_row: str) -> Row:
    row = Row()
    number_indices = [0, 2, 4, 8, 10, 12, 16, 18, 20]
    for index in number_indices:
        number = string_sudoku_row[index]
        if number == " ":
            value = 0
        else:
            value = int(number)
        row.add_cell(value)
    return row