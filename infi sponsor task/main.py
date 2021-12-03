things = []
line_ind = 0
with open('dataset.txt', 'r') as file:
    for line in file:
        if line_ind == 0:
            line_ind += 1
            continue
        thing = dict()
        thing['name'] = line.split(':')[0]
        thing['components'] = []
        for component in line.split(':')[1].strip().split(', '):
            thing['components'].append({
                'name': component.strip().split()[1],
                'amount': int(component.strip().split()[0])
            })
        thing['details'] = 0
        things.append(thing)

def calculate(name):
    print(name)
    has_been_found = False
    for thing in things:
        if thing['name'] == name:
            if thing['details'] != 0:
                return thing['details']
            has_been_found == True
            for component in thing['components']:
                thing['details'] += component['amount'] * calculate(component['name'])
            return thing['details']
    
    if not has_been_found:
        return 1    

print(things)
for thing in things:
    calculate(thing['name'])
print(things)

print(max(things, key=lambda x: x['details']))



