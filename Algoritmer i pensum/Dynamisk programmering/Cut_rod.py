import math

#Kun iterativ implementasjon, uten DP!

def cut_rod(p,n):
    if n == 0:
        return 0

    q = -math.inf
    for i in range(1,n+1):
        q = max(q, p[i-1] + cut_rod(p,n-i))

    return q

def main():
    p = [1,5,8,9,10,17,17,20,24,30];    n = 9

    print("Maksimal fortjeneste med n = "+str(n)+" er: ", end="")
    print(cut_rod(p,n))

main()
