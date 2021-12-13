import numpy as np


with open("../data/input_13.txt") as file:
    paper = file.read()

paper_dots = paper.split('\n\n')[0]
paper_folds = paper.split('\n\n')[1]

# Create list of tuples for paper dots
paper_dots = paper_dots.split('\n')
paper_dots = list(map(lambda x: (int(x.split(',')[0]),int(x.split(',')[1])), paper_dots))

# Create list of tuples in format ('x/y', 'foldline')
paper_folds = paper_folds.split('\n')
paper_folds = list(map(lambda x: (x.split('=')[0][-1], int(x.split('=')[1])), paper_folds))

# Create numpy array for paper dots and populate using list of tuples
x_max = max([x[0] for x in paper_dots])
y_max = max([x[1] for x in paper_dots])
paper_map = np.zeros((x_max + 1,y_max + 1), dtype=int)
for i in paper_dots:
    paper_map[i] += 1

def fold_paper(np_array, fold_line, axis):
    #slice paper into two sections and flip
    if axis == 'x':
        paper_back = np_array[:fold_line,:].copy()
        paper_front = np_array[fold_line+1:,:].copy()
        folded = np.flip(paper_front, axis=0) + paper_back
    elif axis == 'y':
        paper_back = np_array[:,:fold_line].copy()
        paper_front = np_array[:,fold_line+1:].copy()
        folded = np.flip(paper_front, axis=1) + paper_back
    return np.where(folded > 1, 1, folded)

answer_1 = fold_paper(paper_map, paper_folds[0][1], paper_folds[0][0]).sum()

print("Answer to part 1 is: {}".format(answer_1))


# Part 2
def complete_all_folds(paper_map, paper_folds):
    p = paper_map.copy()
    for i in paper_folds:
        p = fold_paper(p, i[1], i[0])
    return p
answer_2 = np.array2string(np.transpose(complete_all_folds(paper_map, paper_folds)), separator='')
print(f"""
Answer to part 1 is:
{answer_2}
""")




