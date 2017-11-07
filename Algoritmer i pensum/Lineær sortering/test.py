B = [[1,2,3],[4,5,6],[9,8,7]]

C = []
C += C.extend(b for b in B)

print(C)
