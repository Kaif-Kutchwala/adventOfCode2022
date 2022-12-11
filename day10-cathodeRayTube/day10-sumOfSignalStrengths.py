file = open("day10-input.txt", "r")
commands = file.read().splitlines()

clock_cycle = 1
X = 1
signal_strengths = []
cooldown = 0
command_index = 0
add_pending = (False, 0)
ll = []
clock_cycle_next_check = 20
result = ""
current_row = 0

while clock_cycle <= 240:
    try:
        command = commands[command_index]
    except IndexError:
        command = "done"

    print(X, clock_cycle, cooldown, add_pending, command_index)

    if clock_cycle == clock_cycle_next_check:
        ll.append((X, clock_cycle))
        signal_strengths.append(X*(clock_cycle))
        clock_cycle_next_check += 40

    if add_pending[0]:
        X += add_pending[1]
        add_pending = (False, 0)

    if cooldown:
        clock_cycle += 1
        cooldown -= 1
        continue

    if command == "noop":
        pass
    elif command.split(" ")[0] == "addx":
        amount = int(command.split(" ")[1])
        add_pending = (True, amount)
        cooldown = 1
    else:
        pass

    command_index += 1
    clock_cycle += 1

print(signal_strengths)
print(ll)
print(sum(signal_strengths))
