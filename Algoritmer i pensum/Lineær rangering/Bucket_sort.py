

def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        B[int(n*A[i])].insert(-1, A[i])

    for j in range(n):
        insertion_sort(B[j])

    res = []
    for i in range(len(B)):
        res += (B[i])

    return res



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
    unsorted_list = [0.103,0.552,0.246,0.733,0.942]
    sorted_list = bucket_sort(unsorted_list)
    print(sorted_list)





main()
