from sys import stdin

__author__ = "Henrik Høiness"

#Velger så mange av den største mynten, så nest størst osv
def min_coins_greedy(coins, value):
    min_coins = 0
    for coin in coins:
        if value>=coin:
            min_coins += value//coin
            value = value%coin

    return min_coins


def min_coins_dynamic(coins, value, length):
    inf = 1000000000
    # Lager en antall minimum mynter
    # Starter på 0, så må legge til en på value
    min_coins = [inf]*(value+1)
    # Dersom noen skal "veklse" 0 kr
    min_coins[0] = 0

    for i in range(1,value+1):
        for j in range(length):
            if coins[j] == i:
                min_coins[i] = 1

            elif coins[j] < i:
                # Før den aktuelle mynten blir lagt til
                sub_resultat = min_coins[i-coins[j]]
                # Om antall mynter nå er mindre enn det som var i tabellen fra før av
                if sub_resultat != inf and sub_resultat+1 < min_coins[i]:
                    min_coins[i] = sub_resultat+1

    return min_coins[-1]


def can_use_greedy(coins):
    for i in range(1,len(coins)):
        if coins[i]%coins[i-1] != 0:
            return False
    return True

coins = sorted([int(c) for c in input().split()], reverse=True)
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line),len(coins)))
