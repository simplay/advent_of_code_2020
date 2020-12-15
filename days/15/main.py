from collections import defaultdict


def find_last_spoken_number(sequence: list, number_of_turns: int):
    ages = defaultdict(lambda: [])

    for turn in range(len(sequence)):
        ages[sequence[turn]] = [turn]

    last_number_spoken = 0
    ages[last_number_spoken].append(len(sequence))

    for turn in range(len(sequence) + 1, number_of_turns):
        turns_of_spoken_numbers = ages[last_number_spoken]

        if len(turns_of_spoken_numbers) == 1:
            last_number_spoken = 0
        else:
            last_number_spoken = turns_of_spoken_numbers[-1] - turns_of_spoken_numbers[-2]

        ages[last_number_spoken].append(turn)

    return last_number_spoken


if __name__ == "__main__":
    sequence = [1, 12, 0, 20, 8, 16]
    spoken_number = find_last_spoken_number(sequence=sequence, number_of_turns=2020)
    print("Task 1:", spoken_number)

    spoken_number = find_last_spoken_number(sequence=sequence, number_of_turns=30000000)
    print("Task 2:", spoken_number)
