from functools import reduce


# borrowed from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * invert_modulo(p, n_i) * p
    return sum % prod


# Extended Euclid
def extended_euclid(a: int, b: int):
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
    >>> extended_euclid(7, 5)
    (-2, 3)
    """
    if b == 0:
        return 1, 0
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return y, x - k * y


def invert_modulo(a: int, n: int) -> int:
    """
    >>> invert_modulo(2, 5)
    3
    >>> invert_modulo(8,7)
    1
    """
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


def find_id_earlies_bus(arrival_time: int, bus_ids_with_unknowns: list):
    bus_ids = [int(bus_id) for bus_id in bus_ids_with_unknowns if bus_id.isdigit()]
    arrival_time = int(arrival_time)

    next_departure_times = [arrival_time - (arrival_time % bus_id) + bus_id for bus_id in bus_ids]
    time_till_bus_departures = [(next_departure_time - arrival_time) for next_departure_time in
                                next_departure_times]

    bus_list = zip(bus_ids, time_till_bus_departures)

    bus_id, delta_time = min(bus_list, key=lambda bus: bus[1])

    return bus_id, delta_time


def find_earlies_timestamp(bus_ids_with_unknowns: list):
    remainders = []
    modulos = []

    for bus_list_idx in range(len(bus_ids_with_unknowns)):
        bus_id = bus_ids_with_unknowns[bus_list_idx]

        if not bus_id.isdigit():
            continue

        # bus_id + bus_list_idx = 0 mod (bus_id)
        # modulo := bus_id and remainder := -bus_list_idx mod (bus_id)
        bus_id = int(bus_id)
        modulos.append(bus_id)
        remainder = (-bus_list_idx) % bus_id
        remainders.append(remainder)

    return chinese_remainder(modulos, remainders)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().splitlines()
        arrival_time, bus_ids_with_unknowns = lines
        bus_ids_with_unknowns = bus_ids_with_unknowns.split(",")

        bus_id, delta_time = find_id_earlies_bus(arrival_time, bus_ids_with_unknowns)
        earliest_timestamp = find_earlies_timestamp(bus_ids_with_unknowns)

        print(f"Task 1: {bus_id * delta_time}")
        print(f"Task 2:", earliest_timestamp)
