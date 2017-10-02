from sys import stdin

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    rotnode = Node()
    for ord, posisjon in ordliste:
        current_node = rotnode

        for character in ord:
            if character not in current_node.barn:
                current_node.barn[character] = Node()

            current_node = current_node.barn[character]
        current_node.posi += [posisjon]

    return rotnode


def posisjoner(ord, indeks, node):
    character = ord[indeks]

    word_end = (indeks == len(ord)-1)

    if character in node.barn:
        if word_end:
            return node.barn[character].posi
        return posisjoner(ord,indeks+1,node.barn[character])

    elif character == '?':
        res_pos = []
        for key in node.barn:
            if word_end:
                res_pos += node.barn[key].posi
            else:
                res_pos += posisjoner(ord,indeks+1,node.barn[key])

        return res_pos

    return []




def main():
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append((o, pos))
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print("%s:" % sokeord, end = "")
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print(" %s" % p, end = "")
        print()


if __name__ == "__main__":
    main()
