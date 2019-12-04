puzzle_input_min = 156218
puzzle_input_max = 652527


def find_password(range_min, range_max):
    password = []
    for i in range(range_min, range_max):
        if is_ascending(i) and has_double(i):
            password.append(i)
    return password


def is_ascending(num):
    for index, n in enumerate(str(num)):
        if index != 0:
            if int(n) < int(last_n):
                return False
        last_n = n

    return True


def has_double(num):
    for index, n in enumerate(str(num)):
        for j, nu in enumerate(str(num)):
            if index != j:
                if n == nu:
                    return True

    return False


def main():
    print(len(find_password(puzzle_input_min, puzzle_input_max)))


if __name__ == '__main__':
    main()
