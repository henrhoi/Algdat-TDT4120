from sys import stdin

__author__ = "Henrik Høiness"


# Fjern før kok
stdin = open("input1.txt")

# Capasities (kapasiteter) er den originale kapasitet-matrisen som er en n x n element-liste hvor n er antall noder
# Start_room er en liste over indekser til noder som korresponderer til startrommene
# Exits er en liste over indekser til noder som korresponderer med utganger.


def isolated_path_count(capacities, start_rooms, exits):
    # Du kan bruke metoden find_flow_paths() for å forenkle oppgaven.
    C = utvid(capacities, start_rooms, exits)
    n = len(C) # antall noder
    F = [] # flyt
    for i in range(n):
        F.append([0] * n)
    antallStier = 0
    superkilde = 0
    supersluk = n - 1
    while True:
        # Finn en sti det kan sendes flyt langs
        sti = find_flow_paths(superkilde, supersluk, F, C)
        if not sti:
            return "%d" % antallStier
        # Oppdaterer flyten langs stien

        for i in range(len(sti)-1):
            # find_flow_paths() har garantert bare funnet en flyt på 1
            F[sti[i]][sti[i+1]] += 1
            F[sti[i+1]][sti[i]] -= 1
        antallStier += 1

        if antallStier == len(start_rooms):
            return "%d" % antallStier

def utvid(C, startrom, exits):
    n = len(C)
    # Vi skal splitte alle noder og legge paa en superkilde og et supersluk
    # -> 2 * tidligere lengde + 2
    new_n = 2 * n + 2
    # Lager en liste av lister med den utregnede dimensjonen
    new_C = []
    for i in range(new_n):
        new_C.append([0] * new_n)

    # Først fyller vi inn hvilke superkilden skal ha kapasiteter til:
    for i in startrom:
        # Siden vi splitter noder skal denne til inn-noden for et gitt rom
        new_C[0][i*2+1] = 1

    # Så tar vi for oss de tidligere kapasitetene
    for i in range(n):
        for j in range(n):
            new_C[2*i+2][2*j+1] = C[i][j]

    # Så fyller vi inn slik at vi har 1 i kapasitet mellom
    # de to splittede nodene som representerer ett rom
    for i in range(n):
        new_C[2*i+1][2*i+2]=1

    # Til slutt setter vi inn hvilke rom som er utganger
    for i in exits:
        new_C[2*i+2][new_n-1] = 1

    return new_C


def check(adj):
    for i in range(len(adj)):
        if adj[i][i] != 0:
            print('nm[%d][%d] != 0' % (i, i))

        for j in range(len(adj)):
            if adj[i][j] != adj[j][i]:
                print('nm[%d][%d] != nm[%d][%d]' % (i, j, j, i))


# Finner en vei fra kilden til sluk. med tilgjengelig kapasitet i et flyt-nettverk med flyt F og kapasitet C
# Returnerer en liste der det første elementet er indexen til en av startnodene, siste element er indeksen til en av
# utgangene, og elementene i mellom er indeksene til nodene langs veien, i korrekt rekkefølge.
# Eksempel: En vei fra start node 4 til node 3, node 9, node 7 og til slutt til utgangen node 12 vil bli
# representert som [4,3,9,7,12]


def find_flow_paths(source, drain, F, C):
    n = len(F)
    discovered = [False] * n
    parend = [None] * len(F)
    koe = [source]
    while koe:
        node = koe.pop(0)

        if node == drain:
            # Har funnet sluken, lager en array med passerte noder
            path = []
            i = node
            while True:
                path.append(i)
                if i == source:
                    break
                i = parend[i]
            path.reverse()
            return path;

        for neighbour in range(n):
            if not discovered[neighbour] and F[node][neighbour] < C[node][neighbour]:
                koe.append(neighbour);
                discovered[neighbour] = True;
                parend[neighbour] = node;
    return None


nodes, _, _ = [int(x) for x in stdin.readline().split()]
start_rooms = [int(x) for x in stdin.readline().split()]
exits = [int(x) for x in stdin.readline().split()]
adj_matrix = []
for linje in stdin:
    n_row = [int(neighbour) for neighbour in linje.split()]
    adj_matrix.append(n_row)

print(isolated_path_count(adj_matrix, start_rooms, exits))
