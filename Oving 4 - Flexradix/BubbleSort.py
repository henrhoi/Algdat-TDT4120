from sys import stdin
__author__ = "Henrik Høiness"


def BubbleSort(inList):
    list_length = len(inList) - 1
    unsorted = True

    while unsorted:
        unsorted = False                    # Har denne utenfor for-løkka
        for index in range(0,list_length):
            if inList[index] > inList[index + 1]:
                temp = inList[index + 1]
                inList[index + 1] = inList[index]
                inList[index] = temp
                # print(badList)            # Kommenterte ut denne når jeg ble ferdig å teste
                unsorted = True             # Dersom listen er sortert, stop while-løkken




def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    BubbleSort(strings)
    for string in strings:
        print(string)


if __name__ == "__main__":
    main()
