import re
from functools import reduce

if __name__ == "__main__":
    blank_line_regex = r"(?:\r?\n){2,}"
    with open("input.txt") as file:
        content = file.read()
        lines = re.split(blank_line_regex, content)

        letters_in_word = lambda word: set(list(word))
        group_answers = lambda group: [letters_in_word(word) for word in group.strip().split("\n")]

        unions = [reduce(lambda x, y: x.union(y), group_answers(line)) for line in lines]
        intersections = [
            reduce(lambda x, y: 1 if y is None else x.intersection(y), group_answers(line)) for line in lines
        ]

        print("Task 1", sum([len(union) for union in unions]))
        print("Task 2", sum([len(intersection) for intersection in intersections]))
