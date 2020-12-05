def index_value(encoding):
    chars = list(encoding)
    char_count = len(chars)

    lower_bound = 0
    upper_bound = 2 ** char_count

    # binary search
    for char_index in range(char_count):
        middle_value = 2 ** (char_count - char_index - 1)
        if ("F", "L").__contains__(chars[char_index]):
            upper_bound -= middle_value
        else:
            lower_bound += middle_value

    return lower_bound


if __name__ == "__main__":

    seat_ids = []
    with open("input.txt") as file:
        for line in file.readlines():
            normalized_line = line.strip()

            row_encoding = normalized_line[:-3]
            column_encoding = normalized_line[-3:]

            row_value = index_value(row_encoding)
            column_value = index_value(column_encoding)

            # seat hash function
            seat_id = row_value * 8 + column_value
            seat_ids.append(seat_id)

    # sort seat ids to easily find max seat id and our seat id.
    seat_ids.sort()
    print("Task 1 - Highest seat ID:", seat_ids[-1])

    for idx in range(len(seat_ids) - 1):
        left = seat_ids[idx]
        right = seat_ids[idx + 1]

        # the seats with IDs + 1 and -1 from yours will be in your list
        if right - left == 2:
            print("Task 2 - Our seat ID:", left + 1)
