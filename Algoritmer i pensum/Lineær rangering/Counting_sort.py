

# A = usortert liste, B = sortert output (først tom), k = største tall i A, C = Counter
def counting_sort(A,k):
    res = [0]*len(A)
    count = [0 for _ in range(k+1)]

    for j in range(0,len(A)):
        count[A[j]] += 1

    # C[i] inneholder nå antall forekomster av element i

    for i in range(1,k+1):
        count[i] += count[i-1]
    # Count er nå kumulativ sum
    # C[i] inneholder nå antall elementer mindre eller lik i

    # Itererer baklengs gjennom A, for at Counting blir stabil. Trekker fra en på count når vi plasserer et element
    for j in range(len(A)-1,-1,-1):
        element = A[j]

        res[count[element]-1] = element
        count[element] -= 1

    return res



def main():
    A = [3,5,2,6,1,7,9,8,4]
    sorted_list = counting_sort(A,9)
    print(sorted_list)

main()






