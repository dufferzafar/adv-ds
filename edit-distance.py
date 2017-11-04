"""Edit Distance between two strings."""


def edit_distance(x, y, cost):

    m, n = 1 + len(x), 1 + len(y)

    # Build an m x n list for storing the result
    R = [[-1] * n for _ in range(m)]

    # When len(x) == 0 (or x = "")
    for j in range(n):
        # no other way but to insert all characters of y
        R[0][j] = cost["insert"] * j

    # Similarly, when len(y) == 0 (or y = "")
    for i in range(m):
        # we'll have to delete all the characters of x
        R[i][0] = cost["delete"] * i

    # Go over each character of strings x & y
    for i in range(1, m):
        for j in range(1, n):

            # Costs of various ways of making the strings equal
            costs = []

            # Copy is only possible when the characters match
            if x[i-1] == y[j-1]:  # account for 0 based string indexing
                costs.append(cost["copy"] + R[i-1][j-1])

            # Other ways are always possible

            # Replace
            costs.append(cost["replace"] + R[i-1][j-1])

            # Insert
            costs.append(cost["insert"] + R[i-1][j])

            # Delete
            costs.append(cost["delete"] + R[i][j-1])

            # We want the way that returns the minimum
            R[i][j] = min(costs)

    return R[m-1][n-1]
