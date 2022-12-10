letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

file = open("day3-input.txt", "r")
lines = file.read().splitlines()
priority_score = 0

for i in range(0, len(lines), 3):
    group = lines[i: i + 3]
    badge = set.intersection(*map(set, group))
    priority_score += letters.index(badge.pop()) + 1

print(priority_score)
file.close()