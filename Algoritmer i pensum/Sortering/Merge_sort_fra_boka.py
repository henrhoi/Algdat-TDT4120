import math

__author__ = "Henrik Høiness"

# skjønner idéen men får feil

def Merge_sort(A,p,r):
    if p<r:
        q = (p+r)//2
        Merge_sort(A,p,q)
        Merge_sort(A,q+1,r)
        Merge(A,p,q,r)



# Subliste fra liste A[0..p..q..r]
def Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q

    L = [None for _ in range(n1+1)]
    R = [None for _ in range(n2+1)]

    for i in range(n1):
        L[i] = A[p+i-1]

    for j in range(n2):
        R[j] = A[q+j]

    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0

    for k in range(p,r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1




def main():
    A = [3,5,2,6,99,8,4]; p = 0; r = len(A)-1
    Merge_sort(A,p,r)
    print(A)

main()
