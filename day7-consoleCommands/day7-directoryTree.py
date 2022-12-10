import sys
from Tree import Tree
sys.setrecursionlimit(50)

def isCommand(line : str):
    return line[0] == "$"

def isCd(line: str):
    return isCommand and line[2:4] == "cd"

file = open("day7-input.txt", "r")
terminalCommands = file.read().splitlines()   
file_structure = Tree()
for line in terminalCommands:
    if not isCommand(line):
        size, name = line.split(" ")
        if size != "dir":
            file_structure.add_node(name, int(size))
    
    if isCd(line):
        to_directory = line.split(" ")[-1]
        if to_directory == "..":
            file_structure.go_up()
        else:
            file_structure.add_node(to_directory)

file_structure.update_sizes()

print(sum(filter(lambda x: x.size <= 100000, file_structure.dirs)))