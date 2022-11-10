import numpy as np


def min_path(matrix):
    dp_matrix = np.zeros(np.shape(matrix), dtype=np.int8)
    
    rows = np.shape(dp_matrix)[0]
    columns = np.shape(dp_matrix)[1]

    for i in range(1, rows):
        dp_matrix[i][0] = dp_matrix[i - 1][0] + matrix[i][0]
    
    for j in range(1, columns):
        dp_matrix[0][j] = dp_matrix[0][j - 1] + matrix[0][j]

    for i in range(1, rows):
        for j in range(1, columns):
            dp_matrix[i][j] = min(dp_matrix[i - 1][j], dp_matrix[i][j - 1]) + matrix[i][j]
    
    return dp_matrix[rows - 1][columns - 1]
def main(file):
    with open(file, 'r') as f:
        rows = 0
        a = []
        for line in f:
            line = line.strip()
            for index in range(len(line)):
                a.append(int(line[index]))
            rows += 1
            columns = len(line)
        arr = np.array(a, dtype=np.int8).reshape(rows, columns)
        print(min_path(arr)) 



if __name__ == '__main__':
    # main('dataset_train.txt')  
    main('dataset.txt') 
    #main('dataset_train.txt')
    #main('dataset.txt') 