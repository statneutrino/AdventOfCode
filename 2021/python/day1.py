from statistics import mean

# Read file as list
with open("../data/input_1.txt") as file:
   depths = file.read().splitlines()
depths = list(map(int, depths))

# PART 1
# Create tuple pairs and iterate
depth_tuples = list(zip(depths[:-1], depths[1:]))
depth_inc_counter = 0    
for i in depth_tuples:
    if i[1] > i[0]:
        depth_inc_counter += 1

print("Answer to part 1 is: {}".format(depth_inc_counter))

# Create three-measurement window pairs in tuples
windows = list(zip(depths[:-2], depths[1:-1], depths[2:]))
depth_window_tuples = list(zip(windows[:-1], windows[1:]))

depth_inc_counter = 0    
for i in depth_window_tuples:
    if mean(i[1]) > mean(i[0]):
        depth_inc_counter += 1

print("Answer to part 2 is: {}".format(depth_inc_counter))