import numpy as np


def fold_paper(paper, folds):
    new_paper = np.copy(paper)
    for fold in folds:
        if fold.get('x') != None:
            for x in range(fold['x'] + 1):
                for y in range(new_paper.shape[0]):
                    try:
                        if new_paper[y][fold['x'] + x] == 1:
                            new_paper[y][fold['x'] - x] = new_paper[y][fold['x'] + x]
                    except Exception:
                        pass
            new_paper = new_paper[0:new_paper.shape[0], 0:fold['x']]
        else:
            for x in range(new_paper.shape[1]):
                for y in range(fold['y'] + 1):
                    try:
                        if new_paper[fold['y'] + y][x] == 1:
                            new_paper[fold['y'] - y][x] = new_paper[fold['y'] + y][x]
                    except Exception:
                        pass
            new_paper = new_paper[0:fold['y']][::]
    return new_paper


def start_count(array: np.array):
    count = 0
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            if array[x, y] == 1:
                count += 1
    return count


def main(file, size_x, size_y):
    with open(file, 'r') as f:
        paper = np.zeros(size_y*size_x, np.int8).reshape(size_y, size_x)    
        folds = []
        for line in f:
            if line == '\n':
                break
            paper[int(line.strip().split(',')[1])][int(line.strip().split(',')[0])] = 1    
        

        for line in f:
            folds.append({line.strip().split()[2].split('=')[0]:int(line.strip().split()[2].split('=')[1])})
        
        print(start_count(fold_paper(paper, [folds[0]])))
        new_paper = fold_paper(paper, folds)
        # first 7 letters 
        print(new_paper[::, :35])
        # last letter
        print(new_paper[::, 35:])

if __name__ == '__main__':
    # main('dataset_train.txt', 11, 15) # 5 9
    main('dataset.txt', 1311, 895) # 4573 117509