

def parent(i):
    return i//2

def left(i):
    return 2*i

def right(i):
    return 2*i +1


def max_heapify(A,i):
    l = left(i)
    r = right(i)

    #Dersom venstre barn er mindre A.heapsize og venstre barn er større enn i
    if l <= len(A) and A[l] > A[i]:
        # setter største av de tre elementene til å være venstre barn
        largest = l

        # Hvis ikke er node i større
    else:
        largest = i

    #Dersom venstre barn er mindre A.heapsize og venstre barn er større enn largest
    if r <= len(A) and A[r] > A[largest]:
        # Setter største til å være høyre barn
        largest = r

    #Dersom et av barna er størst, bytt plass med i og kall rekursivt på barnet
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest)



def build_max_heap(A):
    for i in range(len(A)//2,-1,-1):
        max_heapify(A,i)


def main()
    A = [4,1,3,2,16,9,10,14,8,7]

    build_max_heap(A)

    print(A)
