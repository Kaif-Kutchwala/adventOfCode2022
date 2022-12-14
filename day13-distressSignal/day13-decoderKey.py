import functools

file = open("day13-input.txt", "r")
lines = file.read().splitlines()

def get_packets(lines: list[str]):
    packets = []
    for line in lines:
        if line != "":
            packet = eval(line)
            packets.append(packet)
    return packets

packets= get_packets(lines)

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left < right else 0 if left == right else -1

    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    
    if isinstance(left, list) and isinstance(right, list):
        index = 0
        while index < len(left) and index < len(right):
            order = compare(left[index], right[index])
            
            if order in [1,-1]:
                return order
            
            index += 1
        
        if index == len(left):
            if len(left) == len(right):
                return 0
            return 1
        
        return -1


def solve(packets):
    packets.append([[2]])
    packets.append([[6]])

    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)
    print(sorted_packets)

    indices = []
    for i, packet in enumerate(sorted_packets, 1):
        if [[2]] == packet:
            indices.append(i)
        
        if [[6]] == packet:
            indices.append(i)

    print(indices)
    print(functools.reduce(lambda x,y: x*y, indices))


solve(packets)

    