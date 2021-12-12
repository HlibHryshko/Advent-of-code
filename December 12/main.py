def graph_traverse1(graph, vertex, visited):
    count = 0
    # loop through all the vertices connected with the current one
    for vert in graph[vertex]:
        # if the vertex is end then just increment the count by 1
        if vert == 'end':
            count += 1

        # else if the vertex starts with lowercase(small cave)
        elif vert[0].islower():
            # if the vertex that we want to visit is not yet visited
            if visited[vert] == 0:
                # create copy of the dictionary(In Python, if you change the variable, which was assigned from the other dictionary, both of them will change)
                visited_copy = visited.copy()
                visited_copy[vert] = 1
                # increase the count by the count of the recursion call
                count += graph_traverse1(graph, vert, visited_copy)
            
        else:
            # increase the count byt the count of the recursion call
            count += graph_traverse1(graph, vert, visited)
    # return the count of different pathes
    return count


def graph_traverse2(graph, vertex, visited):
    count = 0
    # loop through all the vertices connected with the current one
    for vert in graph[vertex]:
        # if the vertex is end then just increment the count by 1
        if vert == 'end':
            count += 1

        # else if the vertex starts with lowercase(small cave)
        elif vert[0].islower():
            # creatig the copy of the dictionary
            visited_copy = visited.copy()
            visited_copy[vert] += 1
            amount = 0
            # counting the amount of 2-times visited caves
            for val in visited_copy.values():
                if val == 2:
                    amount += 1
            # if the amount of the vertices visited twice is 1 or 0 and the amount this vertex was visited is 2 or 1
            if amount < 2 and visited_copy[vert] < 3:
                # increase the count byt the count of the recursion call
                count += graph_traverse2(graph, vert, visited_copy)
            
        else:
            # increase the count byt the count of the recursion call
            count += graph_traverse2(graph, vert, visited)
     # return the count of different pathes
    return count


def main(file):
    with open(file, 'r') as f:
        graph = {}
        visited = {}

        for line in f:
            args = line.strip().split('-')
            # if any of the points is lower case then append the point as a key to dictionary with value 0
            if args[0][0].islower():
                visited[args[0]] = 0
            if args[1][0].islower():
                visited[args[1]] = 0
            # if the starting point of the node is not end and if the ending point of the node is not start
            if args[0] != 'end' and args[1] != 'start':
            # then check if there is this vertex in the graph dictionary
            # if yes, then just append the second vertex to all the vertices, which the first one is connected with
            # if no, then create new key with the array, where the first element is the second vertex
                if graph.get(args[0]) != None:
                    graph[args[0]].append(args[1])
                else:
                    graph[args[0]] = [args[1]]
            # repeat the same acitons as for the first one
                if graph.get(args[1]) != None:
                    graph[args[1]].append(args[0])
                else:
                    graph[args[1]] = [args[0]]
        
        print(graph_traverse1(graph, 'start', visited))
        print(graph_traverse2(graph, 'start', visited))

if __name__ == '__main__':
    main('dataset_train0.txt') # 5 9
    main('dataset_train1.txt') # 10 36
    main('dataset_train2.txt') # 19 103
    main('dataset_train3.txt') # 226 3509
    main('dataset.txt') # 4573 117509