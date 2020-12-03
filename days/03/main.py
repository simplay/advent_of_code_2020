from functools import reduce

if __name__ == "__main__":
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]

    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file.readlines()]

        grid_height = len(grid)
        grid_width = len(grid[0])

        tree_collision_counts = []
        for slope in slopes:
            right_index, down_index = slope
            tree_collision_count = 0

            while down_index < grid_height:
                if grid[down_index][right_index % grid_width] == '#':
                    tree_collision_count += 1

                right_index += slope[0]
                down_index += slope[1]

            tree_collision_counts.append(tree_collision_count)

        print("Tree hits task 1: ", tree_collision_counts[1])
        print("Collision factor task 2: ", reduce(lambda x, y: x * y, tree_collision_counts))
