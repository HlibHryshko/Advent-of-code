def part1(file):
    with open(file, 'r') as f:
        for line in f:
            coords = [int(i) for i in line.split(',')]
        max_coords = max(coords)
        min_fuel = 999999999
        for x in range(max_coords):
            sum = 0
            for coord in coords:
                sum += abs(x - coord)
            if sum < min_fuel:
                min_fuel = sum
    print(min_fuel)
        

def part2(file):
    with open(file, 'r') as f:
        for line in f:
            coords = [int(i) for i in line.split(',')]
        max_coords = max(coords)
        min_fuel = 999999999
        for x in range(max_coords):
            sum = 0
            for coord in coords:
                num = abs(x - coord)
                sum += (num * (num + 1)) // 2
            if sum < min_fuel:
                min_fuel = sum
        print(min_fuel)

if __name__ == '__main__':
    part1('dataset_train.txt')
    part1('dataset.txt')
    part2('dataset_train.txt')
    part2('dataset.txt')