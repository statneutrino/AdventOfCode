with open("../data/input_8.txt") as file:
   segments = [(x.split(' | ')[0], x.split(' | ')[1]) for x in file.read().splitlines()]

# Part 1
def determine_code(pattern):
    pattern = pattern.split(' ')
    one_code = frozenset([x for x in pattern[list(map(len, pattern)).index(2)]])
    four_code = frozenset([x for x in pattern[list(map(len, pattern)).index(4)]])
    seven_code = frozenset([x for x in pattern[list(map(len, pattern)).index(3)]])
    eight_code = frozenset([x for x in pattern[list(map(len, pattern)).index(7)]])
    return {one_code:1, four_code:4, seven_code:7, eight_code:8}

determine_code(segments[0][0])

counter = {1:0, 4:0, 7:0, 8:0}
for i in range(len(segments)):
    four_digit = list(map(lambda x: frozenset([i for i in x]), segments[i][1].split()))
    code_dict = determine_code(segments[i][0])
    for j in map(code_dict.get, four_digit, four_digit):
        for k in counter.keys():
            if j == k:
                counter[j] +=1

print("Answer to part 1 is: {}".format(sum(counter.values())))

# Part 2
def determine_full_code(pattern):
    pattern = pattern.split(' ')
    
    # Determine 1, 4, 7, 8
    one_code = frozenset([x for x in pattern[list(map(len, pattern)).index(2)]])
    four_code = frozenset([x for x in pattern[list(map(len, pattern)).index(4)]])
    seven_code = frozenset([x for x in pattern[list(map(len, pattern)).index(3)]])
    eight_code = frozenset([x for x in pattern[list(map(len, pattern)).index(7)]])
    
    # Determine 5-character (2, 3, 5)
    char_5 = [set(x) for x in filter(lambda x: len(x)==5, pattern)]
    # Determine 6-character (0, 6, 9)
    char_6 = [set(x) for x in filter(lambda x: len(x)==6, pattern)]
    
    # Determine top 
    top = seven_code - one_code
    
    # Determine bottom and left_lower
    left_corner = set(eight_code - four_code.union({top}))
    bottom = left_corner.copy()
    for i in char_5:
        bottom -= bottom - i
    left_lower = left_corner - bottom
    
    # Determine 2, 3, 5
    two_code = frozenset([x for x in char_5 if not left_lower.intersection(x) == set()][0])
    char_5 = [x for x in char_5 if left_lower.intersection(x) == set()]
    if char_5[0].intersection(one_code) == one_code:
        three_code, five_code = (frozenset(char_5[0]), frozenset(char_5[1]))
    else:
        three_code, five_code = (frozenset(char_5[1]), frozenset(char_5[0]))
        
    #Determine 0, 6, 9    
    nine_code = frozenset([x for x in char_6 if left_lower.intersection(x) == set()][0])
    char_6 = [x for x in char_6 if not left_lower.intersection(x) == set()]
    if len(char_6[1].intersection(seven_code)) == 2:
        zero_code, six_code = (frozenset(char_6[0]), frozenset(char_6[1]))
    else:
        zero_code, six_code = (frozenset(char_6[1]), frozenset(char_6[0]))
    return {zero_code:0,
            one_code:1, 
            two_code:2,
            three_code:3,
            four_code:4,
            five_code:5,
            six_code:6,
            seven_code:7, 
            eight_code:8,
            nine_code:9
    }

def find_total():
    total = 0
    for i in range(len(segments)):
        four_digit = list(map(lambda x: frozenset([i for i in x]), segments[i][1].split()))
        code_dict = determine_full_code(segments[i][0])
        value = int(''.join(map(lambda x: str(code_dict.get(x)), four_digit))) 
        total += value

    return total

print("Answer to part 2 is: {}".format(find_total()))