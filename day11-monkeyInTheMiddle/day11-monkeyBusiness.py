file = open("day11-input.txt", "r")
lines = file.read().splitlines()

monkey_items : list[list[int]] = []
monkey_operations: list[list[str, int]] = []
monkey_test: list[list[int,int,int]] = []
monkey_move_count : list[int] = []

def perform_operation(value, operation, amount) -> int:
    if amount == "old":
        amount = value

    if operation == "*":
        return value * amount
    
    elif operation == "/":
        return value // amount
    
    elif operation == "+":
        return value + amount

    elif operation == "-":
        return value - amount
    
    return value


for i in range(0, len(lines), 7):
    starting_items = lines[i+1].split(":")[-1].strip().replace(" ", "").split(",")
    monkey_items.append([int(x) for x in starting_items])

    operation, amount = lines[i+2].split(" ")[-2:]
    amount = int(amount) if amount.isdigit() else "old"
    monkey_operations.append((operation, amount))

    test_number = int(lines[i+3].split(" ")[-1])
    true_monkey = int(lines[i+4].split(" ")[-1])
    false_monkey = int(lines[i+5].split(" ")[-1])
    monkey_test.append((test_number, true_monkey, false_monkey))

    
monkey_move_count = [0 for _ in monkey_items]
for _ in range(20):
    for monkey_id, monkey_item in enumerate(monkey_items):
        for index, item in enumerate(monkey_item):
            operation, amount = monkey_operations[monkey_id]
            worry_level = perform_operation(item, operation, amount) // 3
            monkey_move_count[monkey_id] += 1
            
            test_number, true_monkey, false_monkey = monkey_test[monkey_id]
            if worry_level % test_number == 0:
                monkey_items[true_monkey].append(worry_level)
            else:
                monkey_items[false_monkey].append(worry_level)
        monkey_items[monkey_id] = []

monkey_move_count.sort()
print(monkey_move_count[-1]* monkey_move_count[-2])