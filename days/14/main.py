import re


def version1(lines):
    mem = {}
    mask = list(36 * "X")
    for line in lines:
        action, value = line.split(" = ")

        if action == "mask":
            mask = list(value.strip())
        else:
            address = re.match(r"mem\[(\d+)\]", action).groups(1)[0]

            binary_number = "{0:b}".format(int(value))
            leading_zeros = "0" * (36 - len(binary_number))
            binary_number = f"{leading_zeros}{binary_number}"

            masked_value = []
            for (value_bit, mask_bit) in zip(list(binary_number), mask):
                if mask_bit == "X":
                    masked_value.append(value_bit)
                else:
                    masked_value.append(mask_bit)

            mem[address] = list(masked_value)

    return mem


def compute_addresses(generator_address: str):
    candidates = [""]

    for digit in list(generator_address):
        new_candidates = []
        appends = ["0", "1"] if digit == "X" else [digit]

        for candidate in candidates:
            for append in appends:
                new_candidates.append(f"{append}{candidate}")

        candidates = new_candidates

    return candidates


def version2(lines):
    mem = {}
    mask = list(36 * "X")
    for line in lines:
        action, value = line.split(" = ")

        if action == "mask":
            mask = list(value.strip())
        else:
            address = re.match(r"mem\[(\d+)\]", action).groups(1)[0]

            binary_number = "{0:b}".format(int(address))
            leading_zeros = "0" * (36 - len(binary_number))
            binary_number = f"{leading_zeros}{binary_number}"

            masked_address = []
            for (value_bit, mask_bit) in zip(list(binary_number), mask):
                if mask_bit == "0":
                    masked_address.append(value_bit)
                else:
                    masked_address.append(mask_bit)

            for address in compute_addresses("".join(masked_address)):
                binary_number = "{0:b}".format(int(int(value)))
                mem[address] = binary_number

    return mem


def compute_checksum(memory):
    checksum = 0
    for _, value in memory.items():
        number = int("".join(value), 2)
        if number > 0:
            checksum += number

    return checksum


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().splitlines()

        checksum1 = compute_checksum(version1(lines))
        print("Task 1", checksum1)

        checksum2 = compute_checksum(version2(lines))
        print("Task 2", checksum2)
