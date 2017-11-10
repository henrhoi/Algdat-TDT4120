from sys import stdin

__author__ = "Henrik Høiness"

# Må fjernes før levering
stdin = open("input.txt")

def best_path(nm, prob):
    ferdig = [False] * n
    ksans = [0.0] * n  # kummulativ sannsynlighet
    ksans[0] = prob[0]
    forrige = [x for x in range(n)]
    beste_node = 0
    for i in range(n):
        node = beste_node
        ferdig[node] = True
        hoyeste_ksans = -1.0
        for nabo in range(n):
            if not ferdig[nabo]:
                if nm[node][nabo] == 1:
                    tilbud = ksans[node] * prob[nabo]
                    if tilbud > ksans[nabo]:
                        forrige[nabo] = node
                        ksans[nabo] = tilbud
                if ksans[nabo] > hoyeste_ksans:
                    beste_node = nabo
                    hoyeste_ksans = ksans[nabo]
    if ksans[-1] == 0.0:
        return '0'
    index = n - 1
    sti = []
    while index != 0:
        sti.append(index)
        index = forrige[index]
    sti.append(0)
    return '-'.join(map(str, reversed(sti)))


n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print (best_path(neighbour_matrix, probabilities))
