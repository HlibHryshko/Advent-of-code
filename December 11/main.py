from os import read
import numpy as np
    

def perform_step(matrix: np.array):
    # incrementing all the numbers by 1
    np.add(matrix, 1, out=matrix)

    ready_to_flash = []
    could_flash = np.ones(100).reshape(10, 10)

    # checking if there are octopuses with energy level of 10 or more
    for i in range(10):
        for j in range(10):
            if matrix[i, j] > 9:
                matrix[i, j] = 0
                ready_to_flash.append([i, j])
                could_flash[i, j] = 0
    
    flash_count = 0
    # while there are some octopuses who flashed
    while len(ready_to_flash) > 0:
        flash = ready_to_flash.pop()
        flash_count += 1
        '''
        x - place of the flash
        # - the tiles that are affected
        ###
        #x#
        ###
        '''
        # incrementing energy level of all the neighbours, that haven't flashed
        for i in range(flash[0] - 1, flash[0] + 2):
            for j in range(flash[1] - 1, flash[1] + 2):
                if i >= 0 and i < 10 and j >= 0 and j < 10:
                    if could_flash[i, j] == 1:
                        matrix[i, j] += 1
                        if matrix[i, j]>= 10:
                            matrix[i, j] = 0
                            ready_to_flash.append([i, j])
                            could_flash[i, j] = 0
    return flash_count    
    



def part1(file):
    with open(file, 'r') as f:
        matrix = np.zeros(100, np.int8).reshape(10, 10)        
        i = 0

        for line in f:
            for index in range(10):
                matrix[i][index] = int(line[index])
            i += 1
        
        counter = 0
        for step in range(100):
            counter += perform_step(matrix)
        print(counter)

def part2(file):
    with open(file, 'r') as f:
        matrix = np.zeros(100, np.int8).reshape(10, 10)        
        i = 0

        for line in f:
            for index in range(10):
                matrix[i][index] = int(line[index])
            i += 1
        
        step = 1
        while True:
            if perform_step(matrix) == 100:
                print(step)
                break
            step += 1
    

if __name__ == '__main__':
    part1('dataset_train.txt')
    part1('dataset.txt')
    part2('dataset_train.txt')
    part2('dataset.txt')