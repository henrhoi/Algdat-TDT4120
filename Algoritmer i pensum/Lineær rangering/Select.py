# Kjøretiden er O(n) i worst-case
# FUNGERER FOR NOEN TALLSEKVENSER OG I

__author__ = "Henrik Høiness"


def select(A,k):
    if len(A) == 1: return A[0]
    elif len(A) <= 5: # if length is 5 or less, sort it and return the kth smallest element
        insertion_sort(A)
        return A[k-1]

    S = []
    for i in range(0,len(A),5):
        B = A[i:i+5]
        insertion_sort(B)
        S.append(B)

    x = []
    for i in range(len(S)):
        x.append(select(S[i],3))

    M = select(x,len(A)//10)

    L1, L3 = partition_modified(A,M)

    if k <= len(L1):
        return select(L1,k)

    elif k > len(L1)+1:
        return select(L3,k-len(L1))
    else:
        return A[M]




def partition_modified(A,p):
    hi = [] # hi[i] > p
    lo = [] # hi[i] < p

    for i in range(len(A)):       # walk through all the elements in the Array A.
        if A[i] < A[p]:
            lo = lo + [A[i]]
        else:
            hi = hi + [A[i]]

    return lo,hi


def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        # Plasserer A[j] inn i den sorterte sublisten [0..j-1]
        i = j-1
        while i>=0 and A[i] > key:
            # Flytter hvert element en til høyre, så lenge key<A[i]
            A[i+1] = A[i]
            i -= 1
        # Plasserer key på riktig plass
        A[i+1] = key


def main():
    A = [1,5,4,2,6,7,33,25,76,176,464,243,752,863,65,24,75,86,72,45]
    B = [1,5,4,2,6,7,33,25,76,176,464,243,752,863,65,24,75,86, 72, 45]
    i = 11

    n = len(A)

    insertion_sort(B)
    print("Det "+str(i)+"'te tallet i A er: " + str(B[i-1]))

    print(A)
    print("Select gir at det "+str(i)+"'te tallet i A er: " + str(select(A,i)))

main()
