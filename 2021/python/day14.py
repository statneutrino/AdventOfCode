from collections import Counter


with open("../data/input_14.txt") as file:
    polymer_rules = file.read().splitlines()
starter = polymer_rules.pop(0)
polymer_rules = polymer_rules[1:]
polymer_dict = {}

for x in polymer_rules:
    a, b = x.strip().split(' -> ')
    polymer_dict[a] = b

# Part 1 attempt (memory inefficient solution!)
def gen_polymer(starter, polymer_dict, n):
    for i in range(n):
        if i == 0:
            polymer_result = ''
            poly = starter
        else:
            poly = polymer_result
            polymer_result = ''
        for j in range(len(poly)-1):
            pair = poly[j:j+2]
            new_seq = pair[0] + polymer_dict[pair]
            if j == len(poly)-2:
                new_seq += pair[1]
            polymer_result += new_seq
    return polymer_result
polymer = gen_polymer(starter, polymer_dict, 10)

counts=Counter(polymer).most_common()

answer_1 = counts[0][1] - counts[-1][1]

print("Answer to part 1 is: {}".format(answer_1))

# Part 2 memory efficient
def count_polymer(starter, polymer_dict, n):
    characters = Counter(starter)
    pairs = Counter(starter[i:i + 2] for i in range(len(starter) - 1))

    for step in range(n):
        new = Counter()
        for pair, num in pairs.items():
            if pair in polymer_dict:
                a, b = pair
                c = polymer_dict[pair]
                new[a + c] += num
                new[c + b] += num
                characters[c] += num
            else:
                new[pair] = num
        pairs = new

    return max(characters.values()) - min(characters.values())
answer_2 = count_polymer(starter, polymer_dict, 40)

print("Answer to part 2 is: {}".format(answer_2))
