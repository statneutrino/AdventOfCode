
# Read file as list
with open("./data/input_01.txt") as file:
    lines = file.read().splitlines()

# PART 1 & 2

def num_in_str(x: str):
    digit_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for key in digit_dict.keys():
        if key in x:
            return(digit_dict[key])
    
    return(None)


# Intialise list of calibration values
values = []

# Iterate over lines and collate calibration values
for text in lines:
    
    is_first_digit_word = False
    is_last_digit_word = False

    # Iterate over string to find first numeric chars
    idx = 0
    while idx < len(text) and (not text[idx].isnumeric()):
        idx += 1
        if num_in_str(text[:idx]) is not None:
            is_first_digit_word = True
            break

    if is_first_digit_word:
        first_digit = num_in_str(text[:idx])
    else:
        first_digit = text[idx]
    
    # Iterate over string to find second numeric chars
    idx = len(text) - 1
    while idx > 0 and (not text[idx].isnumeric()):
        idx -= 1
        if num_in_str(text[idx:len(text)]) is not None:
            is_last_digit_word = True
            break

    if is_last_digit_word:
        last_digit = num_in_str(text[idx:len(text)])
    else:
        last_digit = text[idx]

    cal_value = int(str(first_digit) + str(last_digit))
    values.append(cal_value)

print(values)
print(sum(values))

# # PART 1

# # Intialise list of calibration values
# values = []

# # Iterate over lines and collate calibration values
# for text in lines:
    
#     # Iterate over string to find first and last numeric chars
#     idx = 0
#     while idx < len(text) and (not text[idx].isnumeric()):
#         idx += 1

#     first_digit = text[idx]

#     idx = len(text) - 1
#     while idx > 0 and (not text[idx].isnumeric()):
#         idx -= 1

#     last_digit = text[idx]

#     cal_value = int(first_digit + last_digit)
#     values.append(cal_value)

# # print(sum(values))


