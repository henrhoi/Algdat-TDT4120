import random

__author__ = "Henrik Høiness"


def Randomized_Quicksort(A,p,r):
    if p < r:
        q = Randomized_Partition(A,p,r)
        Randomized_Quicksort(A,p,q-1)
        Randomized_Partition(A,q+1,r)



def Randomized_Partition(A,p,r):
    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]

    return Partition(A,p,r)



def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def main():
    A = [3,5,2,6,99,8,4]; p = 0; r = len(A)-1
    Randomized_Quicksort(A,p,r)
    print(A)

main()
