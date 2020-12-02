import re


# example lines:
#
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9: c: ccccccccc
#
# split by input-regex-pattern and create an object with the following members:
# min_repetitions, max_repetitions, letter, password

class Password:
    def __init__(self, first_index: str, last_index: str, letter: str, password: str):
        self.first_index = int(first_index)
        self.last_index = int(last_index)
        self.letter = letter
        self.password = password

    @property
    def min_repetitions(self):
        return self.first_index

    @property
    def max_repetitions(self):
        return self.last_index

    def has_expected_letter_counts(self):
        letter_count = self.password.count(self.letter)
        return self.min_repetitions <= letter_count <= self.max_repetitions

    def has_exactly_one_letter_at_positions(self):
        letters_at_indices = [self.password[self.first_index - 1], self.password[self.last_index - 1]]
        return letters_at_indices.count(self.letter) == 1


if __name__ == "__main__":
    # example: 1-3 a: abcde
    pattern = re.compile(r"(\d+)-(\d+)\s([a-z]):\s([a-z]+)")
    with open("input.txt") as file:
        lines = file.readlines()
        passwords = [Password(*pattern.split(line.strip())[1:-1]) for line in lines]
        valid_passwords_task1 = [password for password in passwords if password.has_expected_letter_counts()]
        valid_passwords_task2 = [password for password in passwords if password.has_exactly_one_letter_at_positions()]

        print("Total passwords: ", len(lines))
        print("Valid passwords task 1: ", len(valid_passwords_task1))
        print("Valid passwords task 2: ", len(valid_passwords_task2))
