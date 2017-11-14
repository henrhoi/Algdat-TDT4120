__author__ = "Henrik Høiness"


def Quicksort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q-1)
        Quicksort(A, q+1, r)


# Algoritmen jobber slik
# ≤x | ≥x | x
def Partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    # Listen blir slik slik:
    # ≤x | x | ≥x
    return i+1


def main():
    A = [3,5,2,6,99,8,4]; p = 0; r = len(A)-1
    Quicksort(A,p,r)
    print(A)

main()


