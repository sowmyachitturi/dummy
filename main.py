from itertools import permutations
def brute_force(cities, distances):
    min_distance = float('inf')
    best_route = None
    for route in permutations(cities):
        route = list(route) + [route[0]]
        distance = 0
        for i in range(len(route) - 1):
            distance += distances[route[i]][route[i + 1]]
        if distance < min_distance:
            min_distance = distance
            best_route = route
    return best_route,min_distance
cities=['A','B','C','D']
distances={
    'A':{'B':4,'C':8,'D':7},
    'B':{'A':4,'C':2,'D':3},
    'C':{'A':8,'B':2,'D':6},
    'D':{'A':7,'B':3,'C':6}
}
route, distance = brute_force(cities, distances)
print("Route using brute force:", route[:-1])
print("Total distance using brute force:", distance)
