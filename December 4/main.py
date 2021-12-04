tables = []
index = -1
tables_index = 0
with open('dataset.txt', 'r') as f:
    for line in f:
        if len(line.split(',')) > 1:
            bingo = line.rstrip().split(',')
        elif line == '\n':
            buffer = [[0, 0, 0, 0, 0] for i in range (5)]
            tables.append(buffer)
            tables_index = 0
            index += 1
        else: 
            tables[index][tables_index] = line.strip().split(' ')
            while '' in tables[index][tables_index] :
                tables[index][tables_index].remove('')
            tables_index += 1

print(bingo)
'''
truth_table = []
for size in range(len(tables)):
    truth_table.append([[False, False, False, False, False] for i in range(5)])

is_done = False

for turn in bingo:
    for index in range(len(tables)):
        if is_done == True:
            break
        for i in range(5):
            for j in range(5):
                if tables[index][i][j] == turn:
                    #print(f'index = {index} element = {tables[index][i][j]} turn = {turn}')
                    truth_table[index][i][j] = True
                    is_done = True
                    for i0 in range(5):
                        if truth_table[index][i0][j] == False:
                            is_done = False
                    if is_done:
                        sum = 0
                        for i0 in range(5):
                            for j0 in range(5):
                                if truth_table[index][i0][j0] == False:
                                    sum += int(tables[index][i0][j0])
                        print(sum * int(turn))
                    is_done = True
                    for j0 in range(5):
                        if truth_table[index][i][j0] == False:
                            is_done = False
                            break
                    if is_done:
                        sum = 0
                        for i0 in range(5):
                            for j0 in range(5):
                                if truth_table[index][i0][j0] == False:
                                    sum += int(tables[index][i0][j0])
                        print(sum * int(turn))
                        break
'''
is_done = False
lose = [i for i in range(len(tables)) ]
truth_table = []
for size in range(len(tables)):
    truth_table.append([[False, False, False, False, False] for i in range(5)])

print('PART 2')
for turn in bingo:
    print(lose)
    remove_buffer = []
    for index in range(len(lose)):
        for i in range(5):
            for j in range(5):
                if tables[lose[index]][i][j] == turn:
                    #print(f'index = {index} element = {tables[index][i][j]} turn = {turn}')
                    truth_table[lose[index]][i][j] = True
                    is_done = True
                    for i0 in range(5):
                        if truth_table[lose[index]][i0][j] == False:
                            is_done = False
                            break
                    if is_done:
                        if len(lose) == 1:
                            sum = 0
                            for i0 in range(5):
                                for j0 in range(5):
                                    if truth_table[lose[index]][i0][j0] == False:
                                        print(f'{lose[index]} {tables[lose[index]][i0][j0]}')
                                        sum += int(tables[lose[index]][i0][j0])
                            print(sum * int(turn))    
                        remove_buffer.append(lose[index])
                    is_done = True
                    for j0 in range(5):
                        if truth_table[lose[index]][i][j0] == False:
                            is_done = False
                            break
                    if is_done:
                        if len(lose) == 1:
                            sum = 0
                            for i0 in range(5):
                                for j0 in range(5):
                                    if truth_table[lose[index]][i0][j0] == False:
                                        print(f'{lose[index]} {tables[lose[index]][i0][j0]}')
                                        sum += int(tables[lose[index]][i0][j0])
                            print(sum * int(turn))
                        remove_buffer.append(lose[index])
    for rem in remove_buffer:
        if rem in lose:
            lose.remove(rem)

