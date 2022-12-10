file = open("day4-input.txt", "r")
lines = file.read().splitlines()
count = 0
for line in lines:
    range1, range2 = line.split(",")[0].split("-"),line.split(",")[1].split("-")
    range1 = list(range(int(range1[0]), int(range1[1]) + 1))
    range2 = list(range(int(range2[0]), int(range2[1]) + 1))
    common_items = set.intersection(*map(set, [range1, range2]))
    
    if len(common_items) > 0:
        count += 1
    
print(count)
file.close()