# PART 1
# file = f = open("day1-input.txt", "r");

# maximum_calories = 0
# current_elf_calories = 0
# for line in file:
#     if line == "\n":
#         if current_elf_calories > maximum_calories:
#             maximum_calories = current_elf_calories
#         current_elf_calories = 0
#         continue
    
#     current_elf_calories += int(line)

# f.close()

# print(maximum_calories)

# PART 2
file = f = open("day1-input.txt", "r");

elf_calories = []
current_elf_calories = 0
for line in file:
    if line == "\n":
        elf_calories.append(current_elf_calories)
        current_elf_calories = 0
        continue
    
    current_elf_calories += int(line)
top_3_elf_calories = sorted(elf_calories)[-3:]
f.close()

print(sum(top_3_elf_calories))


