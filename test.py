x = [51,52,53,54,55]
y = [50.55,48.91,46.94,46.24,46.78]


b0 = 101.997
b1 = -1.021

SSE = 0

for i in range(len(x)):
    SSE += (y[i] - b0 - b1*x[i])**2


print(SSE)


SST = 12.973

print(1 - (SSE/SST))
