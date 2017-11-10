__author__ = "Henrik Høiness"


def merge_sort(A):
    if len(A)>1:
        q = len(A)//2
        lh = merge_sort(A[:q])
        rh = merge_sort(A[q:])
        return merge(lh,rh)

    return A



def merge(lh,rh):
    res = []
    i = 0
    j = 0

    while i<len(lh) and j<len(rh):
        if lh[i] < rh[j]:
            res.append(lh[i])
            i+=1

        else:
            res.append(rh[j])
            j+=1

    if i<len(lh): res.extend(lh[i:])
    if j<len(rh): res.extend(rh[j:])
    return res




def main():
    unsorted_list = [3,5,2,6,99,8,4]
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)

main()
