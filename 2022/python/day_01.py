# Read file as list
with open("2022/data/input_01.txt") as file:
   elf_calories = file.read().splitlines()

elf_calories

# Part 1
cal = 0
elf_totals = []
for i in elf_calories:
    if i != '':
        cal += int(i)
    else:    
        elf_totals.append(cal)
        cal = 0
elf_totals.append(cal)
max(elf_totals)

# Part 2
top_three_sum = 0
for i in range(3):
    top_three_sum += max(elf_totals)
    elf_totals.remove(max(elf_totals))
print(top_three_sum)