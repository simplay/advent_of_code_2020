import math

directions = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1)
]


def turn_left(direction: tuple, degree: int) -> tuple:
    steps = 4 - int(degree / 90)
    return directions[(directions.index(direction) + steps) % 4]


def turn_right(direction: tuple, degree: int) -> tuple:
    steps = int(degree / 90)
    return directions[(directions.index(direction) + steps) % 4]


def rotate_point(position, wp, rotation_count):
    cx = position[0]
    cy = position[1]

    pi_quarters = math.pi / 2

    new_wp = [wp[0], wp[1]]
    sinus_value = math.sin(rotation_count * pi_quarters)
    cosine_value = math.cos(rotation_count * pi_quarters)

    new_wp[0] = new_wp[0] - cx
    new_wp[1] = new_wp[1] - cy

    xnew = new_wp[0] * cosine_value - new_wp[1] * sinus_value
    ynew = new_wp[0] * sinus_value + new_wp[1] * cosine_value

    new_wp[0] = xnew + cx
    new_wp[1] = ynew + cy

    return new_wp


def turn_right2(waypoint: tuple, position: tuple, degree: int) -> tuple:
    steps = 4 - int(degree / 90)

    wp_x = position[0] + waypoint[0]
    wp_y = position[1] + waypoint[1]
    wp_x, wp_y = rotate_point(position, (wp_x, wp_y), steps)

    return (wp_x - position[0], wp_y - position[1])


def turn_left2(waypoint: tuple, position: tuple, degree: int) -> tuple:
    steps = int(degree / 90)

    wp_x = position[0] + waypoint[0]
    wp_y = position[1] + waypoint[1]
    wp_x, wp_y = rotate_point(position, (wp_x, wp_y), steps)

    return (wp_x - position[0], wp_y - position[1])


def solve_task1(actions):
    position = (0, 0)
    direction = (1, 0)

    instructions_task = {
        "N": lambda position, direction, value: [(position[0], position[1] + value), direction],
        "S": lambda position, direction, value: [(position[0], position[1] - value), direction],
        "E": lambda position, direction, value: [(position[0] + value, position[1]), direction],
        "W": lambda position, direction, value: [(position[0] - value, position[1]), direction],
        "L": lambda position, direction, value: [position, turn_left(direction, value)],
        "R": lambda position, direction, value: [position, turn_right(direction, value)],
        "F": lambda position, direction, value: [
            (position[0] + value * direction[0], position[1] + value * direction[1]), direction]
    }

    for (instruction, value) in actions:
        new_position, new_direction = instructions_task[instruction](position, direction, value)
        position = new_position
        direction = new_direction

    return abs(position[0]) + abs((position[1]))


def solve_task2(actions):
    waypoint = (10, 1)
    position = (0, 0)

    instructions_task = {
        "N": lambda position, waypoint, value: [position, (waypoint[0], waypoint[1] + value)],
        "S": lambda position, waypoint, value: [position, (waypoint[0], waypoint[1] - value)],
        "E": lambda position, waypoint, value: [position, (waypoint[0] + value, waypoint[1])],
        "W": lambda position, waypoint, value: [position, (waypoint[0] - value, waypoint[1])],
        "L": lambda position, waypoint, value: [position, turn_left2(waypoint, position, value)],
        "R": lambda position, waypoint, value: [position, turn_right2(waypoint, position, value)],
        "F": lambda position, waypoint, value: [
            (position[0] + value * waypoint[0], position[1] + value * waypoint[1]), waypoint]
    }

    for (instruction, value) in actions:
        new_position, new_direction, new_waypoint = instructions_task[instruction](position, direction, waypoint, value)
        position = new_position
        direction = new_direction
        waypoint = new_waypoint

    return abs(position[0]) + abs((position[1]))


if __name__ == "__main__":
    with open("input.txt") as file:
        actions = [[line[0], int(line[1:])] for line in file.read().splitlines()]

        print("Task 1", solve_task1(actions))
        print("Task 2", solve_task2(actions))
