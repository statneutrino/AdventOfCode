import numpy as np

with open("./data/example_03.txt") as file:
    char_matrix = [list(sub) for sub in file.read().splitlines()]

print(np.chararray(char_matrix))