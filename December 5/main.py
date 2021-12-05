def part1(file, size):
    start = []
    end = []
    with open(file, 'r') as f:
        for line in f:
            start.append({
                'x' :int(line.split('->')[0].split(',')[0]),
                'y': int(line.split('->')[0].split(',')[1])
                })
            end.append({
                'x': int(line.split('->')[1].split(',')[0]),
                'y': int(line.split('->')[1].split(',')[1])
                })
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(0)
    for i in range(len(start)):
        if (start[i]['x'] == end[i]['x']):
            x = start[i]['x']
            for j in range(start[i]['y'], end[i]['y']):
                matrix[x][j] += 1
            for j in range(start[i]['y'], end[i]['y'], -1):
                matrix[x][j] += 1
            matrix[x][end[i]['y']] += 1
        elif (start[i]['y'] == end[i]['y']):
            y = start[i]['y']
            for j in range(start[i]['x'], end[i]['x']):
                matrix[j][y] += 1
            for j in range(start[i]['x'], end[i]['x'], -1):
                matrix[j][y] += 1
            matrix[end[i]['x']][y] += 1 
    count = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] > 1:
                count += 1
    print(count)
        

def part2(file, size):
    start = []
    end = []
    with open(file, 'r') as f:
        for line in f:
            start.append({
                'x' :int(line.split('->')[0].split(',')[0]),
                'y': int(line.split('->')[0].split(',')[1])
                })
            end.append({
                'x': int(line.split('->')[1].split(',')[0]),
                'y': int(line.split('->')[1].split(',')[1])
                })
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(0)
    for i in range(len(start)):
        if (start[i]['x'] == end[i]['x']):
            x = start[i]['x']
            for j in range(start[i]['y'], end[i]['y']):
                matrix[x][j] += 1
            for j in range(start[i]['y'], end[i]['y'], -1):
                matrix[x][j] += 1
            matrix[x][end[i]['y']] += 1
        elif (start[i]['y'] == end[i]['y']):
            y = start[i]['y']
            for j in range(start[i]['x'], end[i]['x']):
                matrix[j][y] += 1
            for j in range(start[i]['x'], end[i]['x'], -1):
                matrix[j][y] += 1
            matrix[end[i]['x']][y] += 1
        else: 
            x_start = start[i]['x']
            x_end = end[i]['x']
            y_start = start[i]['y']
            y_end = end[i]['y']
            if (x_start < x_end):
                if y_start < y_end:
                    for j in range(y_start, y_end + 1):
                        matrix[x_start + j - y_start][j] += 1
                else:
                    for j in range(y_end, y_start + 1):
                        matrix[x_end - j + y_end][j] += 1
            else:
                x_start, x_end = x_end, x_start
                y_start, y_end = y_end, y_start
                if y_start < y_end:
                    for j in range(y_start, y_end + 1):
                        matrix[x_start + j - y_start][j] += 1
                else:
                    for j in range(y_end, y_start + 1):
                        matrix[x_end - j + y_end][j] += 1   
    count = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] > 1:
                count += 1
    print(count)

if __name__ == '__main__':
    part1('dataset_train.txt', 10)
    part1('dataset.txt', 1000)
    part2('dataset_train.txt', 10)
    part2('dataset.txt', 1000)