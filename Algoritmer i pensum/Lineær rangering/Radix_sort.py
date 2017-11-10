
# A = usortert liste, d = antall siffer i elemenetene


def radix_sort(A, d):
    for i in range(d-1,-1,-1):
        # Bruker vlagfri stabil sorterings algoritme
        A = counting_sort(A,9,i)

    return A


# Sorterer større tall ved å se på et siffer.
# k = støste tall (9), i = sifferindeks
def counting_sort(A,k,d):
    res = [0]*len(A)
    count = [0 for _ in range(k+1)]

    for j in range(0,len(A)):
        element = int(str(A[j])[d])
        count[element] += 1

    # C[i] inneholder nå antall forekomster av element i

    for i in range(1,k+1):
        count[i] += count[i-1]
    # Count er nå kumulativ sum
    # C[i] inneholder nå antall elementer mindre eller lik i

    # Itererer baklengs gjennom A, for at Counting blir stabil. Trekker fra en på count når vi plasserer et element
    for j in range(len(A)-1,-1,-1):
        element = A[j]

        res[count[int(str(element)[d])]-1] = element
        count[int(str(element)[d])] -= 1

    return res




def main():
    unsorted_list = [732,552,246,643,929,824,411]; d = 3
    sorted_list = radix_sort(unsorted_list,d)
    print(sorted_list)


main()

