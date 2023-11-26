from typing import List, Set
from collections import Counter


class Cell:
    def __init__(
        self,
        value: int,
        row: "Cluster",
        column: "Cluster",
        square: "Cluster",
        x: int,
        y: int,
    ):
        self._value = value
        self.row = row
        self.column = column
        self.square = square
        self.possible_values = set(range(1, 10))
        self.x = x
        self.y = y

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value
        assert (
            not self.is_solved()
        ), f"Cell({self.x}, {self.y}) has value {self._value}, cannot be overwritten to {value}"
        self.row.dirty = True
        self.column.dirty = True
        self.square.dirty = True

    def remove_possible_values(self, values: Set[int]) -> None:
        for value in values:
            self.remove_possible_value(value)

    def remove_possible_value(self, value: int) -> None:
        if self.is_solved():
            return

        self.possible_values.discard(value)
        if len(self.possible_values) == 1:
            print(f"cell {self.x}, {self.y}, value: {self.value}, overwriting")
            print(f"is solved: {self.is_solved()}")
            self.value = self.possible_values.pop()

    def is_solved(self) -> bool:
        return self.value != 0


class Cluster:
    def __init__(self, name: str):
        self.cells: List[Cell] = []
        self.dirty = True
        self.name = name

    def solve(self):
        self.dirty = False
        impossible_values = set([cell.value for cell in self.cells])
        values_counter = Counter({key: 0 for key in {range(1, 10)} - impossible_values})
        for cell in self.cells:
            if not cell.is_solved():
                is_cell_updated = cell.remove_possible_values(impossible_values)
                # if is_cell_updated:
                #     return
                # for value in cell.possible_values:
                #     values_counter[value] += 1
        # self.check_single_possible_value_in_cluster(values_counter)

    def check_single_possible_value_in_cluster(self, values_counter):
        for value, counter in values_counter.items():
            if counter == 1:
                self.solve_single_possible_value(value)
                break

    def solve_single_possible_value(self, value):
        for cell in self.cells:
            if not cell.is_solved() and value in cell.possible_values:
                cell.value = value
                break


class Sudoku:
    def __init__(self):
        self.rows: List[Cluster] = []
        self.columns: List[Cluster] = []
        self.squares: List[Cluster] = []
        for i in range(9):
            self.rows.append(Cluster(name=f"row_{i}"))
            self.columns.append(Cluster(name=f"column_{i}"))
            self.squares.append(Cluster(name=f"square_{i}"))

    def get_all_dirty_clusters(self) -> List[Cluster]:
        return [
            cluster
            for cluster in self.rows + self.columns + self.squares
            if cluster.dirty
        ]

    def solve(self) -> None:
        while True:
            dirty_clusters = self.get_all_dirty_clusters()
            if not dirty_clusters:
                break
            for cluster in dirty_clusters:
                cluster.solve()
