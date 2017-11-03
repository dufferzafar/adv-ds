"""
Edit Distance between two strings.

x: aaa
y: aaa

ED(x, y) = 0?

"""

# A standard copy function
COST = {
    "copy": 0,
    "insert": 2,
    "replace": 2,
    "delete": 1
}


# A top down recursive solution
def edit_distance_bad(x, y, cost):

    # Recursion termination conditions
    if len(x) == 0:
        return len(y) * cost["insert"]

    if len(y) == 0:
        return len(x) * cost["delete"]

    # Costs of various ways of making the strings equal
    costs = []

    # Copy is only possible when the characters match
    if x[0] == y[0]:
        costs.append(cost["copy"] + edit_distance(x[1:], y[1:], cost))

    # Other ways are always possible

    # Replace
    costs.append(cost["replace"] + edit_distance(x[1:], y[1:], cost))

    # Insert
    costs.append(cost["insert"] + edit_distance(x[1:], y, cost))

    # Delete
    costs.append(cost["delete"] + edit_distance(x, y[1:], cost))

    # We want the way that returns the minimum
    return min(costs)


def edit_distance(x, y, cost):

    m, n = len(x), len(y)

    # Build an m x n list for storing the result
    R = [[0] * n for _ in range(m)]

    # When len(x) == 0 (or x = "")
    for j in range(n):
        # no other way but to insert all characters of y
        R[0][j] = cost["insert"] * j

    # Similarly, when len(y) == 0 (or y = "")
    for i in range(m):
        # we'll have to delete all the characters of x
        R[i][0] = cost["delete"] * i

    # Let's do this right!
    for i in range(m):
        for j in range(n):

            # Costs of various ways of making the strings equal
            costs = []

            # Copy is only possible when the characters match
            if x[i] == y[j]:
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
