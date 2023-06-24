"""
Kata from codewars: https://www.codewars.com/kata/646254375cee7a000ffaa404/train/python
"""

import numpy as np
from collections import Counter


class Matrix:
    def __init__(self, array: list[list], desired_size: int):
        self.array = array
        self.actual_size = len(self.array)
        self.valid_values = range(1, desired_size + 1)
        self.rows = enumerate(self.array, start=1)
        self.columns = enumerate(
            (np.take(self.array, n - 1, axis=1) for n in self.valid_values), start=1
        )

    def is_square(self):
        return all(len(i) == self.actual_size for i in self.array)

    def is_correct_size(self, expected_size):
        return self.actual_size == expected_size

    def _value_out_of_range(self, value, row_index, column_index):
        if value not in self.valid_values:
            matrix_index = f"{row_index},{column_index}"
            return f"{value} at {matrix_index} is not between 1 and {max(self.valid_values)}"

    def _value_repeats_in_row(self, row, row_index):
        counter = Counter(row)
        for value, count in counter.items():
            if count > 1:
                return f"{value} occurs more than once in row {row_index}"

    def _value_repeats_in_column(self, column, column_index):
        counter = Counter(column)
        for value, count in counter.items():
            if count > 1:
                return f"{value} occurs more than once in column {column_index}"

    def values_incorrect(self):
        for row_index, row in self.rows:
            for value_index, value in enumerate(row, start=1):
                value_out_of_range = self._value_out_of_range(
                    value, row_index, value_index
                )
                if value_out_of_range:
                    return value_out_of_range
            value_repeats_in_row = self._value_repeats_in_row(row, row_index)
            if value_repeats_in_row:
                return value_repeats_in_row
        for column_index, column in self.columns:
            value_repeats_in_column = self._value_repeats_in_column(
                column, column_index
            )
            if value_repeats_in_column:
                return value_repeats_in_column


def verify_latin_square(array, m):
    matrix = Matrix(array, m)
    if matrix.is_square():
        if matrix.is_correct_size(m):
            values_are_incorrect = matrix.values_incorrect()
            if values_are_incorrect:
                return values_are_incorrect
            else:
                return f"Valid latin square of size {matrix.actual_size}"
        else:
            return "Array is wrong size"
    else:
        return "Array not square"


if __name__ == "__main__":

    def create_latin_square(n: int):
        row = [i for i in range(1, n + 1)]
        return [row[i:] + row[:i] for i in range(n)]

    n = 100
    latin_square = create_latin_square(n)
    verification = verify_latin_square(latin_square, n)
    print(verification)
