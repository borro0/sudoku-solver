from typing import List


class Cell:
    def __init__(self, value: int):
        self.value: int = value
        self.possible_values = set(range(1, 10))

    def is_solved(self) -> bool:
        return self.value != 0

class Cluster:
    def __init__(self):
        self.cells: List[Cell] = []

    def solve(self):
        possible_values = set(range(1, 10)) - set([cell.value for cell in self.cells])
        for cell in self.cells:
            if not cell.is_solved():
                if len(possible_values) == 1:
                    cell.value = possible_values.pop()

class Column(Cluster):
    pass

class Row(Cluster):
    pass


class Sudoku:
    def __init__(self):
        self.rows: List[Row] = []
        self.columns: List[Column] = []
        self.squares: List[Cluster] = []
        for _ in range(9):
            self.rows.append(Row())
            self.columns.append(Column())
            self.squares.append(Cluster())

    def solve(self) -> None:
        assert len(self.rows) == 9, "Sudoku should contain 9 rows"
        for row in self.rows:
            row.solve()
        for column in self.columns:
            column.solve()
        for square in self.squares:
            square.solve()

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
