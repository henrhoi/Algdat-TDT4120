from sys import stdin

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = mergeSort(alist[:mid])
        righthalf = mergeSort(alist[mid:])

        return merge(lefthalf,righthalf)
    return alist

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
    sorted_list = mergeSort(input_list)
    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))
if __name__ == "__main__":
    main()
