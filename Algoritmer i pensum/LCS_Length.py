import math


def LCS_Length(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0]*n for row in range(m)]
    c = [[0]*(n+1) for row in range(m+1)]


    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = '↖'

            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = '↑'

            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = '←'

    return c, b


def print_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return

    if b[i][j] == '↖':
        print_LCS(b, X, i-1, j-1)
        print(X[i])

    elif b[i][j] == '↑':
        print_LCS(b, X, i-1, j)

    else:
        print_LCS(b, X, i, j-1)


def main():
    X = ['A','B','C','B','D','A','B']
    Y = ['B','D','C','A', 'B', 'A']

    i = len(X)-1
    j = len(Y)-1

    c, b = LCS_Length(X, Y)

    print_LCS(b,X,i,j)

main()
