from collections import defaultdict


# this is too slow...
#
# def extract_arrangements(jolts, active: int):
#     window = [jolt for jolt in jolts if 0 < jolt - active <= 3]
#
#     if not window:
#         return 1
#
#     return sum([extract_arrangements(jolts, active=item) for item in window])

def total_arrangement_count(jolts):
    possibilities = defaultdict(lambda: 0)

    # There is only one possibility when left out with the last jolt value
    possibilities[jolts[-1]] = 1

    for jolt in reversed(jolts[:-1]):
        # The number of possibilities of the current jolt is the number of possibilities of the -1, -2-th and -3-th
        # jolt; if one of those does not exist, add zero
        possibilities[jolt] = possibilities[jolt + 1] + possibilities[jolt + 2] + possibilities[jolt + 3]

    return possibilities[0]


if __name__ == "__main__":
    with open("input.txt") as file:
        jolts = [int(line) for line in file.read().splitlines()]
        jolts.append(0)
        jolts.append(max(jolts) + 3)
        jolts.sort()

        differences = [right - left for left, right in zip(jolts[:-1], jolts[1:])]
        checksum = differences.count(1) * differences.count(3)

        counts = total_arrangement_count(jolts)

        print("Task 1:", checksum)
        print("Task 2:", counts)
