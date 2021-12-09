from types import MappingProxyType


def part1(file):
    table_0 = []
    with open(file, 'r') as f:
        for line in f:
            table_0.append(line.strip())
        ash_sum = 0
        table = []
        for i in range(len(table_0)):
            table.append([])
            for ch in table_0[i]:
                table[i].append(int(ch))
        for i in range(len(table)):
            for j in range(len(table[i])):
                if i > 0 and i < len(table) - 1:
                    if j > 0 and j < len(table[i]) - 1:
                        if table[i][j] < table[i - 1][j] and table[i][j] < table[i][j - 1] and table[i][j] < table[i + 1][j] and table [i][j] < int(table[i][j + 1]):
                            ash_sum += table[i][j] + 1          
                    else:
                        if j == 0:
                            if table[i][j] < table[i - 1][j] and table[i][j] < table[i + 1][j] and table [i][j] < table[i][j + 1]:
                                ash_sum += table[i][j] + 1 
                        elif j == len(table[i]) - 1:
                            if table[i][j] < table[i - 1][j] and table[i][j] < table[i][j - 1] and table[i][j] < table[i + 1][j]:
                                ash_sum += table[i][j] + 1
                else:
                    if i == 0:
                        if j > 0 and j < len(table[i]) - 1:
                            if int(table[i][j]) < int(table[i][j - 1]) and int(table[i][j]) < int(table[i + 1][j]) and int(table [i][j]) < int(table[i][j + 1]):
                                ash_sum += int(table[i][j]) + 1          
                        else:
                            if j == 0:
                                if int(table[i][j]) < int(table[i + 1][j]) and int(table [i][j]) < int(table[i][j + 1]):
                                    ash_sum += int(table[i][j]) + 1 
                            elif j == len(table[i]) - 1:
                                if int(table[i][j]) < int(table[i][j - 1]) and int(table[i][j]) < int(table[i + 1][j]):
                                    ash_sum += int(table[i][j]) + 1
                    else:
                        if j > 0 and j < len(table[i]) - 1:
                            if int(table[i][j]) < int(table[i - 1][j]) and int(table[i][j]) < int(table[i][j - 1]) and int(table [i][j]) < int(table[i][j + 1]):
                                ash_sum += int(table[i][j]) + 1          
                        else:
                            if j == 0:
                                if int(table[i][j]) < int(table[i - 1][j]) and int(table [i][j]) < int(table[i][j + 1]):
                                    ash_sum += int(table[i][j]) + 1 
                            elif j == len(table[i]) - 1:
                                if int(table[i][j]) < int(table[i - 1][j]) and int(table[i][j]) < int(table[i][j - 1]):
                                    ash_sum += int(table[i][j]) + 1
    print(ash_sum)

def basin_size(indexI, indexJ, table):
    basin = [[False for j in range(len(table[i]))] for i in range(len(table))]
    basin[indexI][indexJ] = True
    needed_walk = []
    if indexI > 0:
        if table[indexI - 1][indexJ] != 9:        
            needed_walk.append([[indexI, indexJ], [indexI - 1, indexJ]])
    if indexI < len(table) - 1:
        if table[indexI + 1][indexJ] != 9:
            needed_walk.append([[indexI, indexJ], [indexI + 1, indexJ]]) 
    if indexJ > 0:
        if table[indexI][indexJ - 1] != 9:
            needed_walk.append([[indexI, indexJ], [indexI, indexJ - 1]])
    if indexJ < len(table[indexI]) - 1:
        if table[indexI][indexJ + 1] != 9:
            needed_walk.append([[indexI, indexJ], [indexI, indexJ + 1]]) 
    index = 0
    size = 1
    i = 0
    j = 1
    indexes1 = [0, 0]
    indexes2 = [0, 0]
    while index < len(needed_walk):
        needed_walk = sorted(needed_walk, key=lambda x: table[x[1][i]][x[1][j]])[::]
        # print(needed_walk)
        indexes1 = needed_walk[index][0]
        indexes2 = needed_walk[index][1]
        if table[indexes1[i]][indexes1[j]] < table[indexes2[i]][indexes2[j]] and not basin[indexes2[i]][indexes2[j]]:
            size += 1
            if indexes2[i] > 0:
                if not basin[indexes2[i] - 1][indexes2[j]] and table[indexes2[i] - 1][indexes2[j]] != 9:
                    needed_walk.append([[indexes2[i], indexes2[j]], [indexes2[i] - 1, indexes2[j]]])
            if indexes2[i] < len(table) - 1:
                if not basin[indexes2[i] + 1][indexes2[j]] and table[indexes2[i] + 1][indexes2[j]] != 9:
                    needed_walk.append([[indexes2[i], indexes2[j]], [indexes2[i] + 1, indexes2[j]]]) 
            if indexes2[j] > 0:
                if not basin[indexes2[i]][indexes2[j] - 1] and table[indexes2[i]][indexes2[j] - 1] != 9:
                    needed_walk.append([[indexes2[i], indexes2[j]], [indexes2[i], indexes2[j] - 1]])
            if indexes2[j] < len(table[indexI]) - 1:
                if not basin[indexes2[i]][indexes2[j] + 1] and table[indexes2[i]][indexes2[j] + 1] != 9:
                    needed_walk.append([[indexes2[i], indexes2[j]], [indexes2[i], indexes2[j] + 1]]) 
        needed_walk.remove(needed_walk[index])
        basin[indexes2[i]][indexes2[j]] = True
    return size

def part2(file):
    table_0 = []
    with open(file, 'r') as f:
        for line in f:
            table_0.append(line.strip())
        ash_sum = 0
        basins = []
        table = []
        for i in range(len(table_0)):
            table.append([])
            for ch in table_0[i]:
                table[i].append(int(ch))
        for i in range(len(table)):
            for j in range(len(table[i])):
                if i > 0 and i < len(table) - 1:
                    if j > 0 and j < len(table[i]) - 1:
                        if table[i][j] < table[i - 1][j] and table[i][j] < table[i][j - 1] and table[i][j] < table[i + 1][j] and table [i][j] < int(table[i][j + 1]):
                            basins.append(basin_size(i, j, table))
                    else:
                        if j == 0:
                            if table[i][j] < table[i - 1][j] and table[i][j] < table[i + 1][j] and table [i][j] < table[i][j + 1]:
                                basins.append(basin_size(i, j, table))
                        elif j == len(table[i]) - 1:
                            if table[i][j] < table[i - 1][j] and table[i][j] < table[i][j - 1] and table[i][j] < table[i + 1][j]:
                                basins.append(basin_size(i, j, table))
                else:
                    if i == 0:
                        if j > 0 and j < len(table[i]) - 1:
                            if table[i][j] < table[i][j - 1] and table[i][j] < table[i + 1][j] and table [i][j] < table[i][j + 1]:
                                basins.append(basin_size(i, j, table))    
                        else:
                            if j == 0:
                                if table[i][j] < table[i + 1][j] and table [i][j] < table[i][j + 1]:
                                    basins.append(basin_size(i, j, table))
                            elif j == len(table[i]) - 1:
                                if table[i][j] < table[i][j - 1] and table[i][j] < table[i + 1][j]:
                                    basins.append(basin_size(i, j, table))
                    else:
                        if j > 0 and j < len(table[i]) - 1:
                            if table[i][j] < table[i - 1][j] and table[i][j] < table[i][j - 1] and table [i][j] < table[i][j + 1]:
                                basins.append(basin_size(i, j, table))  
                        else:
                            if j == 0:
                                if table[i][j] < table[i - 1][j] and table [i][j] < table[i][j + 1]:
                                    basins.append(basin_size(i, j, table))
                            elif j == len(table[i]) - 1:
                                if table[i][j] < table[i - 1][j] and table[i][j] < table[i][j - 1]:
                                    basins.append(basin_size(i, j, table))
    max_basins = sorted(basins)
    print(max_basins)
    print(max_basins[-1] * max_basins[-2] * max_basins[-3])

if __name__ == '__main__':
    part1('dataset_train.txt')
    part1('dataset.txt')
    part2('dataset_train.txt')
    part2('dataset.txt')