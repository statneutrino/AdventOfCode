import numpy as np


with open("../data/input_15.txt") as file:
    cave = file.read().splitlines()
cave = np.array([[int(i) for i in x] for x in cave])


def get_adjacents(np_array, position):
    i, j = position
    i_max, j_max = np_array.shape
    adjacents = set()
    
    if i != 0: 
        adjacents.add((i-1,j)) #above
    if i != i_max - 1:
        adjacents.add((i+1,j)) #below
    if j != 0:
        adjacents.add((i,j-1)) #left
    if j != j_max - 1:
        adjacents.add((i,j+1)) #right
    return adjacents


# Part 1 using Dijkstra's algorithm
def find_shortest_path(cave, start_node, dest_node):   
    visited = np.zeros(cave.shape,dtype=bool) # visited nodes stored in boolean numpy array
    distance_matrix = np.full(cave.shape, np.inf,dtype=float) # stored distance is np array
    distance_matrix[start_node] = 0
    current_node = start_node
    while visited[dest_node] == False:
        if visited[current_node] == False:
            adjacent_nodes = get_adjacents(cave, current_node)
            for adj in adjacent_nodes:
                if distance_matrix[current_node] + cave[adj] < distance_matrix[adj]:
                    distance_matrix[adj] = distance_matrix[current_node] + cave[adj]
            visited[current_node] = True
        nodes_min_d = np.where( # find minimum unvisited node
                            np.logical_and(distance_matrix == np.amin(distance_matrix[np.invert(visited)]),
                            np.invert(visited))
                        )
        current_node = (nodes_min_d[0][0], nodes_min_d[1][0])
        if current_node == dest_node:
            return distance_matrix[dest_node]
    return distance_matrix[dest_node]

answer_1 = find_shortest_path(cave, (0,0), (cave.shape[0]-1,cave.shape[1]-1))
print("Answer to part 1 is: {}".format(answer_1))


# Part 2
def create_large_cave(cave):
    old = np.copy(cave)
    result = np.copy(cave)
    for i in range(4):
        new_cols = old + np.ones(cave.shape, dtype=int)
        new_cols = np.where(new_cols > 9, 1, new_cols)
        result = np.c_[result,new_cols]
        old = result[:,-cave.shape[0]:]
    old = result
    for i in range(4):
        new_cols = old + np.ones((cave.shape[0], cave.shape[1]*5), dtype=int)
        new_cols = np.where(new_cols > 9, 1, new_cols)
        result = np.r_[result,new_cols]
        old = result[-cave.shape[0]:,:]    
    return(result)

large_cave = create_large_cave(cave)
answer_2 = find_shortest_path(large_cave, (0,0), (large_cave.shape[0]-1,large_cave.shape[1]-1))
print("Answer to part 2 is: {}".format(answer_2))