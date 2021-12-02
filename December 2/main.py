x = 0
y = 0

# part 1
with open('dataset.txt', 'r') as file:
    for line in file:
        direction = line.split()[0]
        value = int(line.split()[1].strip())
        if direction == 'forward':
            x += value
        elif direction == 'up':
            y -= value
        else:
            y += value

print(x * y)
# part 2
x = 0
y = 0
aim = 0

with open('dataset.txt', 'r') as file:
    for line in file:
        direction = line.split()[0]
        value = int(line.split()[1].strip())
        if direction == 'forward':
            x += value
            y += value * aim
        elif direction == 'up':
            aim -= value
        else:
            aim += value

print(x * y)