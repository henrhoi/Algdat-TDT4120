__author__ = "Henrik Høiness"

# Løkke-invariant: A[0..j-1] er sortert


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
    unsorted_list = [3,5,2,6,99,8,4]
    insertion_sort(unsorted_list)
    print(unsorted_list)


main()
