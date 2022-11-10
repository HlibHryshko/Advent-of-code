def main(file, steps):
    with open(file, 'r') as f:

        for line in f:
            if line == '\n':
                break
            polimer = line.strip()
        
        add_conditions = {}
        for line in f:
            if line != '\n':
                line = line.strip()
                pair = line.split('->')[0].strip()
                addition = line.split('->')[1].strip()
                add_conditions[pair] = [pair[0] + addition, addition + pair[1]]
        
        print(polimer)

        polimers_count = {}
        for index in range(len(polimer) - 1):
            try:
                polimers_count[polimer[index:index + 2]] += 1
            except Exception:
                polimers_count[polimer[index:index + 2]] = 1
        
        for i in range(steps):
            polimers_count_temporary = {}
            for element, value in polimers_count.items():
                try:
                    polimers_count_temporary[add_conditions[element][0]] += value
                except Exception:
                    polimers_count_temporary[add_conditions[element][0]] = value
                
                try:
                    polimers_count_temporary[add_conditions[element][1]] += value
                except Exception:
                    polimers_count_temporary[add_conditions[element][1]] = value
            
            polimers_count = polimers_count_temporary
        

        final_count = {}
        for element, value in polimers_count.items():
            try:
                final_count[element[0]] += value
            except Exception:
                final_count[element[0]] = value
            
            try:
                final_count[element[1]] += value
            except Exception:
                final_count[element[1]] = value
        
        final_count[polimer[0]] += 1
        final_count[polimer[-1]] += 1
        
        for key in final_count.keys():
            final_count[key] //= 2

        final_count = sorted(final_count.values())
        print(final_count[-1] - final_count[0])
                            


if __name__ == '__main__':
    main('dataset_train.txt', 10)
    main('dataset.txt', 10)
    main('dataset_train.txt', 40)
    main('dataset.txt', 40)