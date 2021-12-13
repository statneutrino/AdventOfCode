import numpy as np


with open("../data/input_11.txt") as file:
   octopus_map = file.read().splitlines()
octopus_map = np.array([[int(i) for i in x] for x in octopus_map],dtype=int)
def get_adjacents(octopus_map, position):
    i, j = position
    i_max, j_max = octopus_map.shape
    adjacents = set()
    
    if i != 0: 
        adjacents.add((i-1,j)) #above
    if i != i_max - 1:
        adjacents.add((i+1,j)) #below
    if j != 0:
        adjacents.add((i,j-1)) #left
    if j != j_max - 1:
        adjacents.add((i,j+1)) #right
    if i != 0 and j != 0:             #above-left
        adjacents.add((i-1,j-1))       #above-left
    if i != 0 and j != j_max - 1:     #above-right
        adjacents.add((i-1,j+1))       #above-right
    if i != i_max - 1 and j != 0:     #below-left
        adjacents.add((i+1,j-1))       #below-left
    if i != i_max - 1 and j != j_max - 1:  #below-right
        adjacents.add((i+1,j+1))       #below-right
    return adjacents


class Octopus:
    def __init__(self, octopus_map):
        self.map = octopus_map.copy()
        self.total_flashes = 0
        self.epoch = 0
        self.i_max, self.j_max = octopus_map.shape
    
    def increase_epoch(self, n_epochs):
        for t in range(n_epochs):
            flashed = set()
            self.map += np.ones((10,10), dtype=int)
            self.epoch += 1
            add_flashes = True if np.count_nonzero(self.map > 9) > 0 else False
            self.total_flashes += np.count_nonzero(self.map > 9)
            self.map = np.where(self.map > 9, 0, self.map)
            while add_flashes == True:
                add_flashes = False
                for i in range(self.i_max):
                    for j in range(self.j_max):
                        adjacents = get_adjacents(self.map, (i,j))
                        for adj in adjacents - flashed:
                            if self.map[i,j] != 0 and self.map[adj] == 0:
                                self.map[i,j] += 1
                        # Make flashes and count extra flashes
                if np.count_nonzero(self.map > 9) > 0:
                    add_flashes = True
                self.total_flashes += np.count_nonzero(self.map > 9)
                flashed.update([x for x in zip(np.where(self.map == 0)[0], np.where(self.map == 0)[1])])
                self.map = np.where(self.map > 9, 0, self.map)
                
    def find_synchonisation(self):
        while self.map.sum() != 0:
            self.increase_epoch(1)
        return(self.epoch)


oct_1 = Octopus(octopus_map)
oct_1.increase_epoch(100)

print("Answer to part 1 is: {}".format(oct_1.total_flashes))

oct_2 = Octopus(octopus_map)
total_epochs = oct_2.find_synchonisation()


print("Answer to part 2 is: {}".format(total_epochs))
