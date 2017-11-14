m = 9
n = 9
c = [[None for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,m+1):
    c[i][0] = 0

for j in range(n+1):
    c[0][j] = 0

for lisst in c:
    print(lisst)


a = ["A",'B','C','D']
print(a[:3])
