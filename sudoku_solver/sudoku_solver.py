from dataclasses import dataclass


@dataclass
class Cell:
    value: int = 0


@dataclass
class Row:
    def __init__(self):
        self.cells = []


class Sudoku:
    def __init__(self):
        self.rows = []

    @staticmethod
    def from_string(string_sudoku: str) -> 'Sudoku':
        sudoku = Sudoku()
        string_sudoku_stripped = string_sudoku.strip().strip("\n")
        lines = string_sudoku_stripped.splitlines()
        for idx, line in enumerate(lines):
            if idx in [3, 7]:
                continue
            row = Sudoku.parse_sudoku_row_string(line)
            sudoku.rows.append(row)
        return sudoku
    
    @staticmethod
    def parse_sudoku_row_string(string_sudoku_row: str) -> Row:
        row = Row()
        number_indices = [0, 2, 4, 8, 10, 12, 16, 18, 20]
        for index in number_indices:
            number = string_sudoku_row[index]
            if number == " ":
                value = 0
            else:
                value = int(number)
            cell = Cell(value)
            row.cells.append(cell)
        return row

    def to_string(self) -> str:
        string_sudoku = ""
        for idx, row in enumerate(self.rows):
            for cell_number, cell in enumerate(row.cells):
                string_sudoku += str(cell.value) + " "
                if cell_number == 2 or cell_number == 5:
                    string_sudoku += "| "
            string_sudoku = string_sudoku.strip()
            string_sudoku += "\n"
            if idx == 2 or idx == 5:
                string_sudoku += "---------------------\n"
        return string_sudoku


def solve_sudoku(string_sudoku):
    sudoku = Sudoku()
    print(string_sudoku)
    sudoku.from_string(string_sudoku)
    result = sudoku.to_string()
    print(result)
    return result
