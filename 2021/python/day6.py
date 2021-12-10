import numpy as np
with open("../data/input_6.txt") as file:
   initial_fish = file.read().split(',')

# Part 1 attempt (which is too heavy on the memory!)
class LanternFish:
    def __init__(self, intial_fish):
        self.fish_states = np.array(initial_fish, dtype=int)
        self.total_fish = len(self.fish_states)
    
    def next_epoch(self, days):
        for i in range(days):
            self.fish_states -= np.ones(self.total_fish, dtype=int)
            index_fish_breeding = np.where(self.fish_states == -1)[0]
            if index_fish_breeding.size >= 1:
                self.fish_states[index_fish_breeding] = 6
                self.fish_states = np.append(self.fish_states, [8] * index_fish_breeding.size)
            self.total_fish = len(self.fish_states)
        return self.fish_states
            
l = LanternFish(initial_fish)
l.fish_states

# Part 2
counts = dict()
for i in map(int, initial_fish):
    counts[i] = counts.get(i, 0) + 1
for i in set(range(9)).difference(set(counts.keys())):
    counts[i] = 0
def simulate_lantern(fish_state_dict, epochs):
    old_states = fish_state_dict.copy()
    for t in range(epochs):
        new_states = dict()
        for i in range(9):
            if i == 6:
                new_states[i] = old_states[7] + old_states[0]
            elif i == 8:
                new_states[i] = old_states[0]
            else:
                new_states[i] = old_states[i+1]
        old_states = new_states.copy()
    return new_states
part1_ans = sum(simulate_lantern(counts, 18).values())
part2_ans = sum(simulate_lantern(counts, 256).values())

print("Answer to part 1 is: {}".format(part1_ans))
print("Answer to part 2 is: {}".format(part2_ans))