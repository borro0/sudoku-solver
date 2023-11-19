from typing import List


class Cell:
    def __init__(self, value: int, row: 'Cluster', column: 'Cluster', square: 'Cluster'):
        self._value = value
        self.row = row
        self.column = column
        self.square = square
        self.possible_values = set(range(1, 10))

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value
        self.row.dirty = True
        self.column.dirty = True
        self.square.dirty = True
        
    def is_solved(self) -> bool:
        return self.value != 0

class Cluster:
    def __init__(self):
        self.cells: List[Cell] = []
        self.dirty = True

    def solve(self):
        possible_values = set(range(1, 10)) - set([cell.value for cell in self.cells])
        for cell in self.cells:
            if not cell.is_solved():
                if len(possible_values) == 1:
                    cell.value = possible_values.pop()

class Sudoku:
    def __init__(self):
        self.rows: List[Cluster] = []
        self.columns: List[Cluster] = []
        self.squares: List[Cluster] = []
        for _ in range(9):
            self.rows.append(Cluster())
            self.columns.append(Cluster())
            self.squares.append(Cluster())

    def solve(self) -> None:
        for row in self.rows:
            row.solve()
        for column in self.columns:
            column.solve()
        for square in self.squares:
            square.solve()


