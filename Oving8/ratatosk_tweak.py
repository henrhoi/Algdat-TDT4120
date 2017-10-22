from sys import stdin

__author__ = "Henrik Høiness"

class Node:
    def __init__(self):
        self.children = []
        self.ratatosk = False
        self.visited = False


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


def main():
    input()
    number_of_nodes = int(input())
    nodes = []
    for i in range(number_of_nodes):
        nodes.append(Node())
    start_node = nodes[int(input())]
    ratatosk_node = nodes[int(input())]
    ratatosk_node.ratatosk = True
    for line in stdin:
        number = line.split()
        temp_node = nodes[int(number.pop(0))]
        for child_number in number:
            temp_node.children.append(nodes[int(child_number)])

    print(dfs(start_node))


main()

