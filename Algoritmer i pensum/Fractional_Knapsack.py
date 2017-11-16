def Fractional_Knapsack(W, v, w):
    kiloprices = [v[i]/w[i] for i in range(len(v))]
    print(kiloprices)
    kiloprices.sort(reverse=True)
    total = 0

    for price in kiloprices:
        total += price*(W//price)
        W -= W%price

    return total



def main():
    w = [10,20,30]
    v = [60,100,120]
    W = 50

    print(Fractional_Knapsack(W,v,w))
main()
