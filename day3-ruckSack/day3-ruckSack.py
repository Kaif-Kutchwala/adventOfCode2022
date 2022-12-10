letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

file = open("day3-input.txt", "r")
priority_score = 0
for line in file:
    length = len(line)
    compartment1_items, compartment2_items = set(line.strip()[: length // 2]), set(line.strip()[(length // 2) :])
    common_item = compartment1_items.intersection(compartment2_items)
    if len(common_item) == 1:
        priority_score += letters.index(common_item.pop()) + 1

print(priority_score)
file.close()
print(letters.index("L") + 1)