import numpy as np
from itertools import combinations


with open("../data/input_5.txt") as file:
   vent_list = file.read().splitlines()

cartersian_points = [[tuple(map(int, y.split(','))) for y in x.split(' -> ')] for x in vent_list]
max_x = max([x[0] for point in cartersian_points for x in point])
max_y = max([y[1] for point in cartersian_points for y in point])
ground = np.zeros((max_x+1, max_y+1), dtype=int)

# Part 1 Find intersections ONLY of horizontal and vertical lines
vertical_lines = [x for x in cartersian_points if x[0][0] == x[1][0]]
horizontal_lines = [x for x in cartersian_points if x[0][1] == x[1][1]]
# Draw vertical lines on ground
for i in vertical_lines:
    x = i[0][0]
    line_range = range(min(i[0][1], i[1][1]), max(i[0][1], i[1][1])+1)
    for j in line_range:
        ground[x,j] += 1
# Draw horizontal lines on ground
for i in horizontal_lines:
    y = i[0][1]
    line_range = range(min(i[0][0], i[1][0]), max(i[0][0], i[1][0])+1)
    for j in line_range:
        ground[j,y] += 1

part1_answer = len(ground[ground > 1])

print("Answer to part 1 is: {}".format(part1_answer))

# Part 2 Now draw diagonal lines
diagonal_lines = [x for x in cartersian_points if (x not in vertical_lines) and (x not in horizontal_lines)]
for i in diagonal_lines:
    x_range = range(i[0][0], i[1][0]+1) if i[0][0] < i[1][0] else range(i[0][0], i[1][0]-1, -1)
    y_range = range(i[0][1], i[1][1]+1) if i[0][1] < i[1][1] else range(i[0][1], i[1][1]-1, -1)
    for i in zip(x_range, y_range):
        ground[i] += 1
part2_answer = len(ground[ground > 1])

print("Answer to part 2 is: {}".format(part2_answer))