from itertools import combinations
from itertools import accumulate


def pairwise_sum_exist(pairs: list, expected_sum: int) -> list:
    for (left, right) in pairs:
        if left + right == expected_sum:
            return [left, right]
    return []


def find_invalid_xmas_number(numbers: list, preamble_length: int) -> int:
    for xmas_index in range(preamble_length, len(numbers)):
        preamble_start_index = xmas_index - preamble_length
        preamble_end_index = xmas_index

        preamble_numbers = numbers[preamble_start_index:preamble_end_index]
        xmas_candidate_number = numbers[xmas_index]
        pairs = combinations(preamble_numbers, 2)

        if not pairwise_sum_exist(pairs, xmas_candidate_number):
            return xmas_candidate_number


def partial_sum_checksum(numbers: list, invalid_number: int) -> int:
    for idx in range(len(numbers) - 1):
        number_subset = numbers[idx:]

        try:
            partial_sum_index = list(accumulate(number_subset)).index(invalid_number)
            partial_sum_numbers = number_subset[:partial_sum_index]
            partial_sum_numbers.sort()
            first_number, *_, last_number = partial_sum_numbers

            return first_number + last_number

        except ValueError:
            pass

    return -1


if __name__ == "__main__":
    with open("input.txt") as file:
        numbers = [int(line) for line in file.read().splitlines()]
        invalid_number = find_invalid_xmas_number(numbers, preamble_length=25)
        print("Task 1:", invalid_number)

        checksum = partial_sum_checksum(numbers, invalid_number)
        print("Task 2:", checksum)
