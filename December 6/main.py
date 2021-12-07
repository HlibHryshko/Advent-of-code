def part1(file):
    with open(file, 'r') as f:
        fishes = []
        for line in f:
            fishes = [int(i) for i in line.strip().split(',')]

        for i in range(80):
            prev_len = len(fishes)
            for index in range(prev_len):
                if fishes[index] == 0:
                    fishes[index] = 6
                    fishes.append(8)
                else:
                    fishes[index] -= 1
        
        print(len(fishes))

        

def part2(file):
     with open(file, 'r') as f:
        fishes = []
        for line in f:
            fishes = [int(i) for i in line.strip().split(',')]
        number_fishes = [0 for i in range(9)]
        for i in range(9):
            fishes_train = [i]
            for j in range(138):
                prev_len =  len(fishes_train)
                for index in range(prev_len):
                    if fishes_train[index] == 0:
                        fishes_train[index] = 6
                        fishes_train.append(8)
                    else:
                        fishes_train[index] -= 1
            number_fishes[i] = len(fishes_train)
            print(f'{i}, {number_fishes[i]}')

        for i in range(118):
            prev_len = len(fishes)
            for index in range(prev_len):
                if fishes[index] == 0:
                    fishes[index] = 6
                    fishes.append(8)
                else:
                    fishes[index] -= 1
        count = 0
        for index in range(len(fishes)):
            count += number_fishes[fishes[index]]
        
        print(count)

if __name__ == '__main__':
    part1('dataset_train.txt')
    part1('dataset.txt')
    part2('dataset_train.txt')
    part2('dataset.txt')