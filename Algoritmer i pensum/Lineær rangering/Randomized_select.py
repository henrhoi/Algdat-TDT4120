import random

# Forventet kjøretid: O(n)
# Worst case: O(n^2)


def randomized_select(A,p,r,i):
    if p == r:
        return A[p]
    q = randomized_partition(A,p,r)
    k = q - p + 1

    # k er antall tall til venstre for q, dvs. at det finnes nøyaktig k tall mindre enn A[q]
    if k == i:
        return A[q]
    elif i < k:
        return randomized_select(A,p,q-1,i)
    else:
        return randomized_select(A,q+1,r,i-k)


def randomized_partition(A,p,r):
    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]

    return partition(A,p,r)


def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def main():
    A = [1,4,6,7,8,11,5]; p = 0; r = len(A)-1
    i = 3

    print(randomized_select(A,p,r,i))

main()

