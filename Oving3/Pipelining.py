#!/usr/bin/python3

from sys import stdin
__author__ = "Henrik Høiness"


def sort_list(inList):
    if inList == []:
        return []
    else:
        pivot = inList[0]
        lesser = sort_list([x for x in inList[1:] if x < pivot])
        greater = sort_list([x for x in inList[1:] if x >= pivot])
        return lesser + [pivot] + greater


def find(A, lower, upper):
    min = binarysearch(A,lower,True)
    max = binarysearch(A,upper,False)
    return [min,max]


def binarysearch(sequence, value, low):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return sequence[mid]
    if value < sequence[0]: return sequence[0]
    if value > sequence[-1]: return sequence[-1]
    if low: return sequence[lo-1]
    return sequence[lo]


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
