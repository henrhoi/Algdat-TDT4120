__author__ = "Henrik Høiness"

# Skal finne i som gir at A[i] == v

# REKURSIV
def Recursive_binary_search(A,p,r,v):
    i = p
    if p < r:
        mid = (p+r)//2
        if v <= A[mid]:
            i = Recursive_binary_search(A,p,mid,v)

        else:
            i = Recursive_binary_search(A,mid+1,r,v)
    return i


# ITERATIV
def Iterative_binary_search(A,p,r,v):
    while p < r:
        mid = (p+r)//2

        if v <= A[mid]:
            r = mid

        else:
            p = mid + 1

    return p



def main():
    A = [1,2,3,6,7,8,9,11,12]; p = 0; r = len(A)-1
    v = 6

    a = Recursive_binary_search(A,p,r,v)
    b = Iterative_binary_search(A,p,r,v)


    print("From Recursive_BS: "+str(a))
    print("From Iterative_BS: "+str(b))

main()
