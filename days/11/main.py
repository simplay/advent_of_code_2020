def simple_grid_update(grid):
    height = len(grid)  # row count
    width = len(grid[0])  # column count

    updated_grid = []
    new_occupied_count = 0
    for row_index in range(height):
        new_row = []
        for column_index in range(width):
            cell = grid[row_index][column_index]

            neighbor_indices = [
                (row_index + 1, column_index),
                (row_index + 1, column_index - 1),
                (row_index + 1, column_index + 1),
                (row_index - 1, column_index),
                (row_index - 1, column_index - 1),
                (row_index - 1, column_index + 1),
                (row_index, column_index + 1),
                (row_index, column_index - 1),
            ]

            occupied_count = 0
            for (neighbor_row_index, neighbor_column_index) in neighbor_indices:
                if 0 <= neighbor_row_index < height and 0 <= neighbor_column_index < width:
                    if grid[neighbor_row_index][neighbor_column_index] == "#":
                        occupied_count += 1

            new_cell = cell
            if cell == "L" and occupied_count == 0:
                new_cell = "#"
            elif cell == "#" and occupied_count >= 4:
                new_cell = "L"

            if new_cell == "#":
                new_occupied_count += 1

            new_row.append(new_cell)

        updated_grid.append(new_row)

    return updated_grid, new_occupied_count


def find_seat(grid: list, position: tuple, direction: tuple) -> str:
    height = len(grid)  # row count
    width = len(grid[0])  # column count

    new_position = (position[0] + direction[0], position[1] + direction[1])
    (row_index, column_index) = new_position
    # print(f"{position}->{new_position}")

    if 0 <= row_index < height and 0 <= column_index < width:
        cell = grid[row_index][column_index]
        if cell == ".":
            return find_seat(grid=grid, position=new_position, direction=direction)
        return cell


def advanced_grid_update(grid):
    directions = [
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        (1, 0),
        (-1, 0),
    ]

    height = len(grid)  # row count
    width = len(grid[0])  # column count

    updated_grid = []
    new_occupied_count = 0
    for row_index in range(height):
        new_row = []
        for column_index in range(width):
            cell = grid[row_index][column_index]
            position = (row_index, column_index)
            neighbors = [find_seat(grid, position, direction) for direction in directions]
            occupied_count = neighbors.count("#")

            new_cell = cell
            if cell == "L" and occupied_count == 0:
                new_cell = "#"
            elif cell == "#" and occupied_count >= 5:
                new_cell = "L"

            if new_cell == "#":
                new_occupied_count += 1

            new_row.append(new_cell)

        updated_grid.append(new_row)

    return updated_grid, new_occupied_count


def number_of_occupied_seats(grid, grid_update_method):
    previous_occupied_count = 0
    while True:
        grid, occupied_count = grid_update_method(grid)
        if previous_occupied_count == occupied_count:
            return occupied_count

        previous_occupied_count = occupied_count


if __name__ == "__main__":
    with open("input.txt") as file:
        grid = [list(line) for line in file.read().splitlines()]

        occupied_count = number_of_occupied_seats(grid, grid_update_method=simple_grid_update)
        print("Task 1:", occupied_count)

        occupied_count = number_of_occupied_seats(grid, grid_update_method=advanced_grid_update)
        print("Task 2:", occupied_count)
