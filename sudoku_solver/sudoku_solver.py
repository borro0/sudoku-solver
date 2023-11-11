from typing import List


class Cell:
    value: int = 0

    def is_solved(self) -> bool:
        return self.value != 0


class Row:
    def __init__(self):
        self.possible_values = set(range(1, 10))
        self.cells: List[Cell] = []

    def add_cell(self, cell: Cell):
        if cell.value != 0:
            self.possible_values.remove(cell.value)
        self.cells.append(cell)

    def solve(self):
        for cell in self.cells:
            if not cell.is_solved():
                if len(self.possible_values) == 1:
                    cell.value = self.possible_values.pop()


class Sudoku:
    def __init__(self):
        self.rows: List[Row] = []

    def solve(self) -> None:
        assert len(self.rows) == 9, "Sudoku should contain 9 rows"
        for row in self.rows:
            row.solve()

    def to_string(self) -> str:
        string_sudoku = ""
        for idx, row in enumerate(self.rows):
            for cell_number, cell in enumerate(row.cells):
                string_value = str(cell.value) if cell.value != 0 else " "
                string_sudoku += string_value + " "
                if cell_number == 2 or cell_number == 5:
                    string_sudoku += "| "
            string_sudoku += "\n"
            if idx == 2 or idx == 5:
                string_sudoku += "--------------------- \n"
        return string_sudoku
