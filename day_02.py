import math

# Read file as list
with open("./data/input_02.txt") as file:
    lines = file.read().splitlines()

# Create dictionary from
games_dict = {}
for line in lines:
    if line.strip():
        game_name, game_data = line.split(': ')
        # Remove spaces from game name
        game_name = int(game_name.replace("Game ", ""))

        # Split the game data into rounds
        rounds = game_data.split('; ')

        round_list = []
        for round in rounds:
            # Split each round into colors and counts
            color_counts = round.split(', ')
            round_dict = {}
            for color_count in color_counts:
                parts = color_count.split(' ')
                if len(parts) == 2:  # To avoid empty strings
                    count, color = parts
                    round_dict[color] = int(count)
            round_list.append(round_dict)

        games_dict[game_name] = round_list

# Determine which games are not possible
max_colours = {
    "red": 12,
    "green": 13,
    "blue": 14
}

impossible = []

for game_n in games_dict.keys():
    for round in games_dict[game_n]:
        for colour in round.keys():
            if round[colour] > max_colours[colour]:
                impossible.append(game_n)
                break

impossible = list(dict.fromkeys(impossible))
possible = set(range(1, 101)) - set(impossible)

# print(sum(possible))

# Find minimum in each game
min_cubes_dict = {}
for game, rounds in games_dict.items():
    color_min = {}
    for round in rounds:
        round_color_counts = {}
        for color, count in round.items():
            round_color_counts[color] = round_color_counts.get(
                color, 0) + count

            # Compare with existing minimums and update
            for color, count in round_color_counts.items():
                if color in color_min:
                    color_min[color] = max(color_min[color], count)
                else:
                    color_min[color] = count

        min_cubes_dict[game] = color_min

#print(min_cubes_dict)
powers = [math.prod(x.values()) for x in min_cubes_dict.values()]
print(sum(powers))
