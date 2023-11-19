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
    for column_number, index in enumerate(number_indices):
        number = string_sudoku_row[index]
        value = int(number) if number != " " else 0
        cell = Cell(value)
        sudoku.rows[row_number].cells.append(cell)
        sudoku.columns[column_number].cells.append(cell)
        sudoku.squares[get_square_number(row_number, column_number)].cells.append(cell)

def convert_sudoku_to_sting(sudoku: Sudoku) -> str:
    string_sudoku = ""
    for idx, row in enumerate(sudoku.rows):
        for cell_number, cell in enumerate(row.cells):
            string_value = str(cell.value) if cell.value != 0 else " "
            string_sudoku += string_value + " "
            if cell_number == 2 or cell_number == 5:
                string_sudoku += "| "
        string_sudoku += "\n"
        if idx == 2 or idx == 5:
            string_sudoku += "--------------------- \n"
    return string_sudoku

def get_square_number(row_number: int, column_number: int) -> int:
    return (row_number // 3) * 3 + column_number // 3