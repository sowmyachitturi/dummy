# Number of vertices in the graph
V = 5
def minKey(key, mstSet):

    min_val = float('inf')
    min_index = -1

    for v in range(V):
        if mstSet[v] == False and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index
def printMST(parent, graph):
    print("Edge \tWeight")
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])



def primMST(graph):
    parent = [None] * V


    key = [float('inf')] * V


    mstSet = [False] * V


    key[0] = 0
    parent[0] = -1


    for count in range(V - 1):

        u = minKey(key, mstSet)


        mstSet[u] = True


        for v in range(V):

            if graph[u][v] and mstSet[v] == False and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]


    printMST(parent, graph)



if __name__ == "__main__":

    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    primMST(graph)
