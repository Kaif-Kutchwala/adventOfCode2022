def isCommand(line : str):
    return line[0] == "$"

def isCd(line: str):
    return isCommand and line[2:4] == "cd"

def findRootDirectory(file_structure, current_directory):
    directories = [x for x in file_structure if current_directory in file_structure[x]]
    print(directories)
    if len(directories):
        return directories[0]
    return "folder:/"

def isDir(line: str):
    return line.split(" ")[0] == "dir"

def getDirectorySize(name: str, file_structure: dict[str, set[str]], file_sizes: dict[str, int]):
    size = 0
    for sub_item in file_structure[name]:
        if sub_item.startswith("folder:"):
            size += getDirectorySize(sub_item, file_structure, file_sizes)
        else:
            size += file_sizes[sub_item]
    return size


def getFileStructure(terminalCommands: list[str]):

    file_structure = {"folder:/" : set([])}
    file_sizes = {}
    current_directory = "folder:/"

    for line in terminalCommands:        

        if not isCommand(line):
            size, name = line.split(" ")
            name = "folder:" + name if isDir(line) else name

            try:
                if name not in file_structure[current_directory]:
                    file_structure[current_directory].add(name)
            except KeyError:
                file_structure[current_directory] = set([name])
            
            if not isDir(line):
                file_sizes[name] = int(size)

            continue

        if isCd(line):
            to_directory = line.split(" ")[-1]

            if to_directory == "..":
                current_directory = findRootDirectory(file_structure, current_directory)
            else:
                current_directory = "folder:" + to_directory 

    return file_structure, file_sizes            





file = open("day7-input.txt", "r")
lines = file.read().splitlines()   
directory_sizes = {}
file_structure, file_sizes = getFileStructure(lines)
print(file_structure, file_sizes)

for directory in file_structure:
    directory_sizes[directory] = getDirectorySize(directory, file_structure, file_sizes)

directories_within_size = [int(x) for x in directory_sizes.values() if int(x) <= 100000]

print(directories_within_size)
print(sum(directories_within_size))