import numpy as np


def hungarian_algorithm(cost_matrix):
    """
    Solves the assignment problem using the Hungarian algorithm.

    Parameters:
        cost_matrix (numpy.ndarray): The cost matrix representing the costs of assigning tasks to workers.

    Returns:
        numpy.ndarray: An array where each element represents the column index of the assigned task for each worker.
    """
    # Step 1: Subtract the minimum value of each row from all elements in that row
    for i in range(len(cost_matrix)):
        min_val = min(cost_matrix[i])
        cost_matrix[i] -= min_val

    # Step 2: Subtract the minimum value of each column from all elements in that column
    for j in range(len(cost_matrix[0])):
        min_val = min(cost_matrix[:, j])
        cost_matrix[:, j] -= min_val

    # Step 3: Cover all zeros in the matrix with the minimum number of lines
    covered_rows = set()
    covered_cols = set()
    while len(covered_rows) + len(covered_cols) < len(cost_matrix):
        zeros = np.argwhere(cost_matrix == 0)
        for row, col in zeros:
            if row not in covered_rows and col not in covered_cols:
                covered_rows.add(row)
                covered_cols.add(col)
                break
        else:
            uncovered_rows = set(range(len(cost_matrix))) - covered_rows
            uncovered_cols = set(range(len(cost_matrix[0]))) - covered_cols
            min_val = float('inf')
            for i in uncovered_rows:
                for j in uncovered_cols:
                    if cost_matrix[i, j] < min_val:
                        min_val = cost_matrix[i, j]
            for i in uncovered_rows:
                cost_matrix[i] -= min_val
            for j in covered_cols:
                cost_matrix[:, j] += min_val

    # Step 4: Find the minimum number of lines to cover all zeros
    zeros = np.argwhere(cost_matrix == 0)
    rows = set(zeros[:, 0])
    cols = set(zeros[:, 1])
    while True:
        new_rows = set()
        for i, j in zeros:
            if j in cols and i not in rows:
                new_rows.add(i)
        if not new_rows:
            break
        rows |= new_rows
        for i, j in zeros:
            if i in rows and j not in cols:
                cols.add(j)
        else:
            continue

    # Step 5: Construct the minimum number of lines and adjust the cost matrix
    covered_rows = set(range(len(cost_matrix))) - rows
    covered_cols = cols
    min_lines = len(covered_rows) + len(covered_cols)
    if min_lines < len(cost_matrix):
        uncovered_rows = rows
        uncovered_cols = set(range(len(cost_matrix[0]))) - cols
        min_val = float('inf')
        for i in uncovered_rows:
            for j in uncovered_cols:
                if cost_matrix[i, j] < min_val:
                    min_val = cost_matrix[i, j]
        for i in uncovered_rows:
            cost_matrix[i] -= min_val
        for j in covered_cols:
            cost_matrix[:, j] += min_val

    # Step 6: Identify the minimum number of lines needed to cover all zeros and the matching
    assignments = {}
    for i, j in zeros:
        if i not in covered_rows and j not in covered_cols:
            assignments[j] = i

    # Convert the assignments to a numpy array
    result = np.zeros(len(cost_matrix), dtype=int)
    for worker, task in assignments.items():
        result[task] = worker

    return result


# Example usage:
cost_matrix = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [25, 35, 45]
])

assignments = hungarian_algorithm(cost_matrix)
print("Assignments:", assignments)
