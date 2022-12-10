file = open("day6-input.txt", "r")

for line in file:
    for i in range(len(line) - 14):
        packet = [line[j] for j in range(i, i + 14)]
        if len(set(packet)) == 14:
            print(i+14)
            break

