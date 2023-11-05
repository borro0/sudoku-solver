from dataclasses import dataclass

@dataclass
class Cell:
    value: int = 0

@dataclass
class Row:
    cells: list[Cell] = None


class Sudoku:
    def __init__(self):
        self.rows = []
    
    def from_string(self, string_sudoku):
        lines = string_sudoku.splitlines()
        for idx,line in enumerate(lines):
            if idx in [3,7]:
                continue
            line = line.replace("|", "")
            row = Row()
            for number in line:
                cell = Cell(int(number))
                row.cells.append(cell)
            self.rows.append(row)
                
        


def solve_sudoku(string_sudoku):
    sudoku = Sudoku()
    sudoku.from_string(string_sudoku)
    return string_sudoku

