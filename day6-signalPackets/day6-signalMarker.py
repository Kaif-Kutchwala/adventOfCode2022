file = open("day6-input.txt", "r")

for line in file:
    for i in range(len(line) - 4):
        packet = [line[j] for j in range(i, i + 4)]
        if len(set(packet)) == 4:
            print(i+4)
            break

