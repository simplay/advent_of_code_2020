from itertools import combinations
from functools import reduce


def compute_hash(expenses: tuple, tuple_count: int) -> int:
    for combination in combinations(expenses, tuple_count):
        if sum(combination) == 2020:
            return reduce(lambda x, y: x * y, combination)


if __name__ == "__main__":
    with open("input_011.txt") as file:
        lines = file.readlines()
        read_expenses = [int(line.strip()) for line in lines]

        print("Solutions:")
        print("Task 1:", compute_hash(expenses=read_expenses, tuple_count=2))
        print("Task 2:", compute_hash(expenses=read_expenses, tuple_count=3))
