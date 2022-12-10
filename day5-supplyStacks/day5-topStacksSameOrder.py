file = open("day5-input.txt", "r")

stack_complete = False
stack_initialised = False
stack = []
for line in file:
    if line == "\n":
        stack_complete = True
        continue
    
    if not stack_complete:
        if len(line) > 2 and line[1] != "1":
            items = list(line[i] for i in range(1, len(line), 4))

            if not stack_initialised:
                for i in range(len(items)):
                    stack.append([])
                stack_initialised = True

            for id, item in enumerate(items):
                    if item != " ":
                        stack[id].insert(0,item)

    if stack_complete:
        digits = [int(item) for item in line.split(" ") if item.replace("\n", "").isdigit()]
        quantity = digits[0]
        origin = digits[1] - 1
        destination = digits[2] - 1
        picked_items = []
        for i in range(quantity):
            picked_items.insert(0,stack[origin].pop())

        for item in picked_items:
            stack[destination].append(item)

ans = [item[-1] for item in stack]
print("".join(ans))
print(stack)     