NUM_LEN = 12
result = [[] for i in range(NUM_LEN)]
with open('dataset.txt', 'r') as file:
    for line in file:
        for i in range(NUM_LEN):
            result[i].append(line.rstrip()[i])

gamma = ''
epsilion = ''
for number in result:
    if number.count('1') > number.count('0'):
        gamma += '1'
        epsilion += '0'
    else:
        gamma += '0'
        epsilion += '1'

gamma = int(gamma, base=2)
epsilion = int(epsilion, base=2)

print(gamma * epsilion)


NUM_LEN = 12
oxygen_array = []
with open('dataset.txt', 'r') as file:
    for line in file:
        oxygen_array.append(line.rstrip())
oxygen = ''
i = 0
numbers = []
while i < NUM_LEN:
    numbers = []
    for num in oxygen_array:
        numbers.append(num[i])
    if numbers.count('1') >= numbers.count('0'):
        oxygen += '1'
    else: 
        oxygen += '0'
    new_oxygen_array = []
    for num in oxygen_array:
        if (num[i] == oxygen[-1]):
            new_oxygen_array.append(num)
    i += 1
    oxygen_array = new_oxygen_array
    if len(oxygen_array) == 1: 
        break


co2_array = []
with open('dataset.txt', 'r') as file:
    for line in file:
        co2_array.append(line.rstrip())
co2 = ''
i = 0
while i < NUM_LEN:
    numbers = []
    for num in co2_array:
        numbers.append(num[i])
    if numbers.count('1') < numbers.count('0'):
        co2 += '1'
    else: 
        co2 += '0'
    
    new_co2_array = []
    for num in co2_array:
        if (num[i] == co2[-1]):
            new_co2_array.append(num)
    i += 1
    co2_array = new_co2_array
    if len(co2_array) == 1: 
        break
oxygen = oxygen_array[0]
co2 = co2_array[0]
oxygen = int(oxygen, base=2)
co2 = int(co2, base=2)

print(oxygen * co2)