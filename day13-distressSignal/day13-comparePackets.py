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
    pairs = [(packets[i], packets[i+1]) for i in range(0, len(packets) - 1 , 2)]
    
    indices = []
    for index, pair in enumerate(pairs, 1):
        left, right = pair
        if (compare(left, right)) == 1:
            indices.append(index)
    
    print(indices)
    print(sum(indices))

solve(packets)

    