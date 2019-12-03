
def find_fuel(fuel):
    return int(fuel / 3) - 2


def calc_fuel(fuel):
    foo = 0
    bar = fuel
    foo = bar
    while find_fuel(bar) > 0:
        bar = find_fuel(bar)
        foo += bar
    return foo


f_sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        fuel = find_fuel(int(line))
        f_sum += calc_fuel(fuel)

print(f_sum)
