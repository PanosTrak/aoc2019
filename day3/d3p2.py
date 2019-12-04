# Collab with https://github.com/GiorT


def main():

    wires = read_file()

    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')

    location1 = draw_wires(wire1)
    location2 = draw_wires(wire2)

    overlap = check_overlap(location1, location2)

    overlap_steps = []

    for i in overlap.values():
        overlap_steps.append(count_steps(location1, i) +
                             count_steps(location2, i))

    print(min(overlap_steps))


def read_file():
    with open('input.txt', 'r') as f:
        wires = f.read().split('\n')
        return wires


def draw_wires(wire):

    xy = (0, 0)
    location = [xy]

    for wi in wire:

        direction = wi[0]
        steps = wi[1:]

        for _ in range(int(steps)):
            if direction == 'U':
                loc_x = location[-1][0]
                loc_y = location[-1][1] + 1
                location.append((loc_x, loc_y))

            elif direction == 'D':
                loc_x = location[-1][0]
                loc_y = location[-1][1] - 1
                location.append((loc_x, loc_y))

            elif direction == 'L':
                loc_x = location[-1][0] - 1
                loc_y = location[-1][1]
                location.append((loc_x, loc_y))

            elif direction == 'R':
                loc_x = location[-1][0] + 1
                loc_y = location[-1][1]
                location.append((loc_x, loc_y))

    return location


def check_overlap(location1, location2):
    overlap_points = {}

    for xy1 in location1:
        for xy2 in location2:
            if xy1 == xy2:
                if xy1[0] is not 0:
                    overlap_points[(abs(xy1[0]) + abs(xy1[1]))] = xy1

    return overlap_points


def count_steps(locations, overlap):
    for i, point in enumerate(locations):
        if point == overlap:
            return len(locations[:i])


if __name__ == '__main__':
    main()
