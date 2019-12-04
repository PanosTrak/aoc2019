def main():

    wires = read_file()

    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')

    location1 = draw_wires(wire1)
    location2 = draw_wires(wire2)

    print(check_overlap(location1, location2))


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
    overlap_points = []

    for loc1 in location1:
        for loc2 in location2:
            if loc1 == loc2:
                if loc1[0] is not 0:
                    overlap_points.append(abs(loc1[0]) + abs(loc1[1]))

    return min(overlap_points)


if __name__ == '__main__':
    main()
