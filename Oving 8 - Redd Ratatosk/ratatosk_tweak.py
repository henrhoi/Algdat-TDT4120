from sys import stdin

__author__ = "Henrik Høiness"

# Dybde-først-søk
def dfs(root):
    stack = [(root,0)]
    if root[1]: return 0
    
    depth = 0
    while len(stack) != 0:
        node = stack.pop()
        
        depth +=1
        for child in node[0][0]:
            if child[1]: return node[1]+1
            if not child[2]:
                child[2] = True
                stack.insert(0,(child,node[1]+1))

def main():
    input()
    number_of_nodes = int(input())
    nodes = []
    for i in range(number_of_nodes):
        nodes.append([[],False,False])
    start_node = nodes[int(stdin.readline())]
    ratatosk_node = nodes[int(stdin.readline())]
    ratatosk_node[1] = True
    for line in stdin:
        number = line.split()
        temp_node = nodes[int(number.pop(0))]
        for child_number in number:
            temp_node[0].append(nodes[int(child_number)])

print(dfs(start_node))

main()
