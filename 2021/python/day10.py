from statistics import median

with open("../data/input_10.txt") as file:
   navigation = file.read().splitlines()


def check_string_valid(bracket_string):
    # Store unclosed brackets
    bracket_list = []
    for char in bracket_string:
        bracket_list.append(char)
        if (
            len(bracket_list) >= 2 and
                (
                    (bracket_list[-2:-1] == ['<'] and bracket_list[-1:] == ['>']) or
                    (bracket_list[-2:-1] == ['['] and bracket_list[-1:] == [']']) or
                    (bracket_list[-2:-1] == ['('] and bracket_list[-1:] == [')']) or
                    (bracket_list[-2:-1] == ['{'] and bracket_list[-1:] == ['}'])
                )
            ):
            del bracket_list[-2:]
    if len(bracket_list) == 0:
        return ("valid", 0)
    for i in bracket_list:
        if i == ')':
            return ("corrupted", 3)
        elif i == ']':
            return ("corrupted", 57)
        elif i == '}':
            return ("corrupted", 1197)
        elif i == '>':
            return ("corrupted", 25137)
    return ("incomplete", 0, bracket_list) # return unclosed brackets as list


total_score = 0
for i in navigation:
    total_score += check_string_valid(i)[1]


print("Answer to part 1 is: {}".format(total_score))

# Part 2
# Scores
# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points
def calculate_incomplete_score(bracket_list):
    total_score = 0
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    bracket_list.reverse()
    for b in bracket_list:
        for key in scores.keys():
            if b == key:
                total_score *= 5
                total_score += scores[b]
    return total_score


unclosed_brackets = [check_string_valid(x)[2]  for x in navigation if check_string_valid(x)[0] == "incomplete"]

score_list = []
for i in unclosed_brackets:
    score_list.append(calculate_incomplete_score(i))
score_list

print("Answer to part 2 is: {}".format(median(score_list)))

