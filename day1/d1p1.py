f_sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        fuel = int(int(int(line) / 3) - 2)
        f_sum += fuel

print(f_sum)
