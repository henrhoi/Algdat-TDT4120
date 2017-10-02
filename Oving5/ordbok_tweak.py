from sys import stdin

def posisjoner(ord, indeks, node,lengde):
    character = ord[indeks]

    word_end = (indeks == lengde)

    if character in node[0]:
        if word_end:
            return node[0][character][1]
        return posisjoner(ord,indeks+1,node[0][character],lengde)

    elif character == '?':
        res_pos = []
        for key in node[0]:
            if word_end:
                res_pos += node[0][key][1]
            else:
                res_pos += posisjoner(ord,indeks+1,node[0][key],lengde)

        return res_pos

    return []

def main():
    pos = 0
    rotnode = ({},[])
    for ord in input().split():
        current_node = rotnode

        for character in ord:
            if character not in current_node[0]:
                current_node[0][character] = ({},[])

            current_node = current_node[0][character]
        current_node[1].append(pos)
        pos += len(ord) + 1

    for sokeord in stdin:
        sokeord = sokeord.strip()
        print("%s:" % sokeord, end = "")
        posi = posisjoner(sokeord, 0, rotnode,len(sokeord)-1)
        posi.sort()
        for p in posi:
            print(" %s" % p, end = "")
        print()

if __name__ == '__main__':
    main()


