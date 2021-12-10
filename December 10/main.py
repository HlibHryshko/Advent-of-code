def part1(file):
    with open(file, 'r') as f:
        elements = [
            ['(', ')', 3], 
            ['[', ']', 57],
            ['{', '}', 1197],
            ['<', '>', 25137]
            ]
        error_sum = 0
        for line in f:
            was_found = False
            line = line.strip()
            buffer = [line[0]]
            for i in range(1, len(line)):
                if was_found:
                    break
                buffer.append(line[i])
                if len(buffer) >= 2:
                    for el in elements:
                        if buffer[-2] == el[0] and buffer[-1] == el[1]:
                            buffer.pop()
                            buffer.pop()
                            break

                if len(buffer) >= 2:
                    for el in elements:
                        if buffer[-1] != '[' and buffer[-1] != '(' and buffer[-1] != '{' and buffer[-1] != '<':
                            if buffer[-2] == el[0] and buffer[-1] != el[1]:
                                for el_error in elements:
                                    if el_error[1] == buffer[-1]:
                                        error_sum += el_error[2]
                                buffer.pop()
                                buffer.pop()
                                was_found = True
                                break
                
        print(error_sum)



def part2(file):
    
    with open(file, 'r') as f:
        elements = [
            ['(', ')', 3, 1], 
            ['[', ']', 57, 2],
            ['{', '}', 1197, 3],
            ['<', '>', 25137, 4]
            ]
        error_sum = 0
        lines = []
        for l in f:
            lines.append([l.strip(), [l[0]], False])
            for line in lines:
                if not line[2]:
                    was_found = False
                    for i in range(1, len(line[0])):
                        line[1].append(line[0][i])
                        if len(line[1]) >= 2:
                            for el in elements:
                                if line[1][-2] == el[0] and line[1][-1] == el[1]:
                                    line[1].pop()
                                    line[1].pop()
                                    break

                        if len(line[1]) >= 2:
                            for el in elements:
                                if line[1][-1] != '[' and line[1][-1] != '(' and line[1][-1] != '{' and line[1][-1] != '<':
                                    if line[1][-2] == el[0] and line[1][-1] != el[1]:
                                        for el_error in elements:
                                            if el_error[1] == line[1][-1]:
                                                error_sum += el_error[2]
                                        line[1].pop()
                                        line[1].pop()
                                        was_found = True
                                        lines.pop()
                                        break
                        if was_found:
                            break
                        else:
                            line[2] = True
        sums = []
        for line in lines:
            sum = 0
            for i in range(len(line[1])):
                for el in elements:
                    if line[1][-1] == el[0]:
                        sum = sum * 5 + el[3]    
                        line[1].pop()
                        break
            sums.append(sum)
        sums = sorted(sums)
        print(sums[len(sums)//2])

if __name__ == '__main__':
    part1('dataset_train.txt')
    part1('dataset.txt')
    part2('dataset_train.txt')
    part2('dataset.txt')