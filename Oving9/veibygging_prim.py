from sys import stdin

__author__ = "Henrik Høiness"

stdin=open("input.txt")

Inf = float(1e3000)

def mst_prim(nm):

    edges = set()           # inneholder (node1, node2)
    verticles = set()       # inneholder noder som er lagt inn i mst

    # Putter inn en vilkårlig startnode
    verticles.add(0)

    while len(verticles) != len(nm):
        possible_edges = []
        for verticle in verticles:
            for neighbour in range(len(nm)):
                if neighbour not in verticles:
                    possible_edges.append((nm[verticle][neighbour],verticle,neighbour))

        # legger til den kanten med minst vekt
        new_edge = min(possible_edges)
        edges.add(new_edge)
        # legger til noden som den nye kanten går til
        verticles.add(new_edge[2])

    # returnerer den dyreste kanten i edges
    return max(edges)[0]


lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
neighbour_matrix = [None] * n
node = 0
for line in lines:
    neighbour_matrix[node] = [Inf] * n
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        neighbour_matrix[node][neighbour] = weight
    node += 1
print (mst_prim(neighbour_matrix))

