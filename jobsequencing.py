def printJobScheduling(arr, n):
    arr.sort(key=lambda x: x[2], reverse=True)

    result = [-1] * n
    slot = [False] * n

    for i in range(n):
        for j in range(min(n, arr[i][1]) - 1, -1, -1):
            if not slot[j]:
                result[j] = i
                slot[j] = True
                break

    for i in range(n):
        if slot[i]:
            print(arr[result[i]][0], end=" ")

# Example usage:
arr = [
    ('a', 2, 100),
    ('b', 1, 19),
    ('c', 2, 27),
    ('d', 1, 25),
    ('e', 3, 15)
]

print("Following is the maximum profit sequence of jobs:")
printJobScheduling(arr, len(arr))
