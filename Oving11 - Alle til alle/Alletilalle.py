from sys import stdin

__author__ = "Henrik Høiness"

maxsize = 9223372036854775807

def shortest_path(order_list, adjacency_matrix, cities):

    #Husk at hun skal returnere til byen hun kom fra!
    order_list.append(order_list[0])

    #Lag kortest vei alle til alle matrise:
    adjacency_matrix = Floyd_Warshall(adjacency_matrix,cities)

    price = 0
    last = order_list[0] #er lik startnoden først
    for city in order_list[1:]:
        if adjacency_matrix[last][city] == maxsize:
            return "umulig"
        else:
            price += adjacency_matrix[last][city]
        last = city
    return price



# Kjøretid O(|V^3|)
def Floyd_Warshall(adj_list, n):
    for k in range(n):  #For hver mellomnode
        for i in range(n):  #For hver rad i matrisen
            for j in range(n):  #For hver element i raden
                adj_list[i][j] = min(adj_list[i][j], adj_list[i][k] + adj_list[k][j])

    return adj_list


testcases = int(stdin.readline())

def main():
    for test in range(testcases):
        cities = int(stdin.readline())
        order_list = [int(by) for by in stdin.readline().split()]
        adj_list = []
        for city in range(cities):
            neighbours = []
            for distance in stdin.readline().split():
                distance = int(distance)
                if distance == -1: distance = maxsize / 3
                neighbours.append(distance)
            adj_list.append(neighbours)
        print(shortest_path(order_list, adj_list, cities))

main()
