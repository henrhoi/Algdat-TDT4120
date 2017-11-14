__author__ = "Henrik Høiness"


def heapsort(A):
    build_max_heap(A)
    heapsize = len(A)
    for i in range(len(A)-1,0,-1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        # Sender inn i = 1, ikke 0 fordi har funksjonene left() og right() som baserer seg på 1-indeksering
        max_heapify(A,heapsize,1)




def build_max_heap(A):
    for i in range(len(A)//2,0,-1):
        max_heapify(A,len(A),i)


def max_heapify(A,heapsize, i):
    l = left(i)
    r = right(i)
    if l <= heapsize and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= heapsize and A[r-1] > A[largest-1]:
        largest = r
    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        max_heapify(A,heapsize,largest)


def parent(i):
    return i//2


def left(i):
    return 2*i


def right(i):
    return 2*i +1


def main():
    A = [4,1,3,2,16,9,10,14,8,7]
    heapsort(A)
    print(A)

main()
