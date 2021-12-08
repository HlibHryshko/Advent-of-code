def part1(file):
    tests = []
    outputs = []
    desired = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip().split('|') 
            tests.append(line[0].strip().split(' '))
            outputs.append(line[1].strip().split(' '))
        
        count = 0
        for i in range(len(tests)):
            # count all the unique numbers in the ouput
            for output in outputs[i]:
                # if the number has unique amount of segments, then increment counter
                if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7: 
                    count += 1
    print(count)
def part2(file):
    tests = []
    outputs = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip().split('|') 
            tests.append(line[0].strip().split(' '))
            outputs.append(line[1].strip().split(' '))
    
    default = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    sum = 0
    for i in range(len(tests)):
        
        possible_235 = []
        possible_069 = []
        
        numbers = ['' for i in range(10)]
        for j in range(10):
            # sorting every number in the list of numbers for the current line
            tests[i][j] = sorted(tests[i][j])
        
        counted = {}
        for letter in default:
            counted[letter] = 0

        shuffled = {}    
        for letter in default:
            shuffled[letter] = ''

        for number in tests[i]:
            # counting the quantity of each segment
            for digit in number:
                counted[digit] += 1
            # putting unique numbers 1, 4, 7, 8 at its place in the numers list
            # putting not unique number in list with numbers of the same length
            if len(number) == 2:
                numbers[1] = number
            if len(number) == 3:
                numbers[7] = number
            if len(number) == 4:
                numbers[4] = number
            if len(number) == 5:
                possible_235.append(number)
            if len(number) == 6:
                possible_069.append(number)
            if len(number) == 7:
                numbers[8] = number
        # getting sorted quantity of segments
        # according to my calculations:
        # 4 : e; 6 : b; 7 : d, g; 8 : a, c; 9 : f
        counted = sorted(counted.items(), key= lambda item: item[1])
        # linking correct segments with shuffled segments accordingly to the quantity
        # counted = [4, 6, 7  , 7  , 8  , 8  , 9]
        # counted = [e, b, d/g, d/g, a/d, a/c, f]
        shuffled['e'] = counted[0][0]
        shuffled['b'] = counted[1][0]
        shuffled['f'] = counted[-1][0]

        # if we find b segment in one of the numbers 2, 3, 5 then it is certainly 5
        # if we find e segment in one of the numbers 2, 3, 5 then it is certainly 2
        # 3 remains after deleting them
        for number in possible_235:
            for letter in range(5):
                if shuffled['e'] == number[letter]:
                    # putting 2 inside the numbers
                    numbers[2] = number 
                if shuffled['b'] == number[letter]:
                    # putting 5 inside the numbers
                    numbers[5] = number
        # deleting 2 and 5 from list with 2, 3, 4
        possible_235.remove(numbers[2])
        possible_235.remove(numbers[5])
        # putting 3 inside the numbers
        numbers[3] = possible_235[0]
        
        # if we find a segment in number 5, which has the quantity of 8(see list counted), then it is certainly a or c
        for letter in numbers[5]:
            if letter == counted[-2][0] or letter == counted[-3][0]:
                if letter == counted[-2][0]:
                    shuffled['a'] = counted[-2][0]
                    shuffled['c'] = counted[-3][0]
                else:
                    shuffled['a'] = counted[-3][0]
                    shuffled['c'] = counted[-2][0]

        # if we find a segment in number 4, which has the quantity of 7(see list counted), then it is certainly d or g
        for letter in numbers[4]:
            if letter == counted[2][0] or letter == counted[3][0]:
                if letter == counted[2][0]:
                    shuffled['d'] = counted[2][0]
                    shuffled['g'] = counted[3][0]
                else:
                    shuffled['d'] = counted[3][0]
                    shuffled['g'] = counted[2][0]
        
        # if we don't find d segment in one of the numbers 0, 6, 9 then it is certainly 0
        # if we don't find c segment in one of the numbers 0, 6, 9 then it is certainly 6
        # if we don't find e segment in one of the numbers 0, 6, 9 then it is certainly 9
        for number in possible_069:
            if shuffled['d'] not in number:
                numbers[0] = number
            if shuffled['c'] not in number:
                numbers[6] = number
            if shuffled['e'] not in number:
                numbers[9] = number

        # putting every number as a list, instead of the list
        for ij in range(len(numbers)):
            numbers[ij] = ''.join(numbers[ij])
        
        # variable for calculating the 4-digit output number
        number = 0
        for output in outputs[i]:
            # sorting the output and then making a line out of it, because sorted returns list object
            output = ''.join(sorted(output))
            # finding the number in our numbers list
            # in this case index it is the number that we need, because of the list design
            ind = numbers.index(output)
            # putting the digit in the end of the number
            number  = number * 10 + ind
        # increasing the sum
        sum += number
    print(sum)

if __name__ == '__main__':
    part1('dataset_train.txt')
    part1('dataset.txt')
    part2('dataset_train.txt')
    part2('dataset.txt')