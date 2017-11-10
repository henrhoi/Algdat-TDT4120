from sys import stdin
from itertools import repeat
__author__ = "Henrik Høiness"


def mergeSort(alist):
    res = ''
    sorted_list = split(alist)
    for i in range(len(sorted_list)):
        res += sorted_list[i][1]

    return res

def split(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = split(alist[:mid])
        righthalf = split(alist[mid:])

        return merge(lefthalf,righthalf)
    return alist[0]

def merge(lefthalf, righthalf):
    res = []

    i=0
    j=0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            res.append(lefthalf[i])
            i=i+1
        else:
            res.append(righthalf[j])
            j=j+1

    if i < len(lefthalf):
        res += lefthalf[i:]
    if j < len(righthalf):
        res += righthalf[j:]
    return res


def main():
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    print(mergeSort(decks))


if __name__ == "__main__":
    main()
