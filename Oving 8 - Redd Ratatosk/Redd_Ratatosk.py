from sys import stdin

__author__ = "Henrik Høiness"

# Node-klasse
class Node:
    def __init__(self):
        self.children = []
        self.ratatosk = False
        self.visited = False

# Dybde-først-søk
def dfs(root):
    stack = [(root,0)]
    if root.ratatosk: return 0

    depth = 0
    while len(stack) != 0:
        node = stack.pop()

        depth +=1
        for child in node[0].children:
            if child.ratatosk: return node[1]+1
            if not child.visited:
                child.visited = True
                stack.insert(0,(child,node[1]+1))


# Bredde-først-søk
def bfs(root):
    if root.ratatosk: return 0
    queue = []

    for child in root.children:
        queue.insert(0,child)

    depth = 1
    while True:
        length = len(queue)
        for i in range(length):
            node = queue[-1]
            if node.ratatosk:
                return depth
            for child in node.children:
                queue.insert(0,child)
            queue.pop()
        depth += 1

def main():
    function = stdin.readline().strip()
    number_of_nodes = int(stdin.readline())
    nodes = []
    for i in range(number_of_nodes):
        nodes.append(Node())
    start_node = nodes[int(stdin.readline())]
    ratatosk_node = nodes[int(stdin.readline())]
    ratatosk_node.ratatosk = True
    for line in stdin:
        number = line.split()
        temp_node = nodes[int(number.pop(0))]
        for child_number in number:
            temp_node.children.append(nodes[int(child_number)])

    if function == 'dfs':
        print(dfs(start_node))
    elif function == 'bfs':
        print(bfs(start_node))
    elif function == 'velg':
        print(dfs(start_node))

main()

