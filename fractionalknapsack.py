from heapq import heappush, heappop

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Comparator:
    def __call__(self, min_item, max_item):
        return max_item.value / max_item.weight > min_item.value / min_item.weight

def fractionalKnapsack(capacity, arr):
    pq = []
    for item in arr:
        heappush(pq, (-item.value/item.weight, item))

    total_value = 0
    while capacity and pq:
        value_weight_ratio, item = heappop(pq)
        value, weight = item.value, item.weight
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value / weight * capacity
            capacity = 0
    return total_value

# Example usage:
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
print("Maximum value in knapsack:", fractionalKnapsack(capacity, arr))
