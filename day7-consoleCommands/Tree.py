class Node():
    def __init__(self, name, parent, size=0) -> None:
        self.name = name
        self.size = size
        self.children : list[Node] = []
        self.parent: Node = parent

    def __str__(self):
        return f"{self.name} ({self.size})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other: int):
        return self.size <= other

    def __ge__(self, other: int):
        return self.size >= other

    def __add__(self, other: int):
        return self.size + other

    def __radd__(self, other: int):
        return self.size + other

class Tree():
    def __init__(self) -> None:
        self.root: Node = Node("/", None)
        self.current_directory: Node = self.root
        self.dirs: list[Node] = []

    def add_node(self, name, size=0):
        if size == 0:
            node = Node(name, self.current_directory)
            self.current_directory.children.append(node)
            self.dirs.append(node)
            self.current_directory = node

        else:
            node = Node(name, self.current_directory, size)
            self.current_directory.children.append(node)

    def go_up(self):
        self.current_directory = self.current_directory.parent

    def update_sizes(self):
        for child in self.root.children:
            self.root.size += self.get_node_size(child)
    
    def get_node_size(self, node: Node):
        for child in node.children:
            node.size += self.get_node_size(child)
        return node.size