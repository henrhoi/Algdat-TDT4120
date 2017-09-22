from sys import stdin
BASE = 26   # Tallsystem (26): 0:a, 1:b ... 25:z


def flexradix(A,index):
    # Dersom lengden av A er mindre eller lik 1, returnerer jeg A
    if len(A)<2:return A

    result = []
    # Lager 26 heaps
    heaps = [[] for base_number in range(BASE)]
    for string in A:
        # Dersom indexen er mindre eller lik lengden til strengen, legger jeg strengen til i resultater
        if index >= len(string):
            result.append(string)
        else:
            # Legger strengen til i en heap med tilhørende verdi(0-25) fra string[index] sin ASCII-verdi minus ASCII-verdien til 'a'
            heaps[ord(string[index]) - ord('a')].append(string)
    # Setter listen med hauger til å være en liste av ett nytt flexradix-kall på alle haugene
    heaps = [flexradix(heap, index+1) for heap in heaps]

    # Legger til alle de resterende strengene i resultatlista med en dobbel for-løkke
    return result + [string for heap in heaps for string in heap]


def main():
    d = stdin.readline()
    # Legger alle strengene inn fra inputfilen i en liste
    strings = [line.rstrip() for line in stdin]

    # Sorterer alle strengene med flexradix()
    sorted_list = flexradix(strings, 0)

    # Printer ut den sorterte listen
    for string in sorted_list:
        print(string)

if __name__ == '__main__':
    main()
