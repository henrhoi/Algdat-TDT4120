# Kjøretiden er O(n) i worst-case

__author__ = "Henrik Høiness"
def select(A, i):
    if len(A) == 1: return A[0]

    elif len(A) <= 5: # if length is 5 or less, sort it and return the kth smallest element
        insertion_sort(A)
        return A[i - 1]

    S = []
    for j in range(0,len(A),5):
        B = A[j:j+5]
        insertion_sort(B)
        S.append(B[len(B)//2])

    M = select(S,len(S)//2)

    L, R = partition_modified(A,M)


    if i == len(L) + 1:
        return M


    elif i < len(L) + 1:
        return select(L, i)


    elif i > len(L)+1:
        return select(R, i - (len(L)+1))




def partition_modified(A,p):
    hi = [] # hi[i] > p
    lo = [] # hi[i] < p

    for i in range(len(A)):       # walk through all the elements in the Array A.
        if A[i] < p:
            lo.append(A[i])
        elif A[i] > p:
            hi.append(A[i])

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
    A = list(range(25))
    B = list(range(25))
    i = 21

    insertion_sort(B)
    print("Det "+str(i)+"'te tallet i A er: " + str(B[i-1]))

    print(A)
    print("Select gir at det "+str(i)+"'te tallet i A er: " + str(select(A,i)))

main()
