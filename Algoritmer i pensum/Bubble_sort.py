__author__ = "Henrik Høiness"

def bubble_sort(A):
    for i in range(0,len(A)):
        for j in range(len(A)-1,i,-1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


def main():
    unsorted_list = [3,5,2,6,99,8,4]
    bubble_sort(unsorted_list)
    print(unsorted_list)


main()
