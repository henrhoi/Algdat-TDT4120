import math



def bottom_up_cut_rod(p,n):
    r = [-math.inf for _ in range(n+1)]
    r[0] = 0

    for j in range(1,n+1):
        q = -math.inf

        for i in range(1,j+1):
            q = max(q, p[i] + r[j-(i+1)])

        r[j] = q
    return r[n]







def main():
    p = [1,5,8,9,10,17,17,20,24,30];    n = 9

    print("Maksimal fortjeneste med n = "+str(n)+" er: ", end="")
    print(bottom_up_cut_rod(p,n))

main()
