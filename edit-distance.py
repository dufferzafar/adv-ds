"""
Edit Distance between two strings.

x: aaa
y: aaa

ED(x, y) = 0?

"""

# A standard copy function
COST = {
    "copy": 0,
    "insert": 1,
    "replace": 1,
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
        costs.append(cost["copy"] + edit_distance_bad(x[1:], y[1:], cost))

    # Other ways are always possible

    # Replace
    costs.append(cost["replace"] + edit_distance_bad(x[1:], y[1:], cost))

    # Insert
    costs.append(cost["insert"] + edit_distance_bad(x[1:], y, cost))

    # Delete
    costs.append(cost["delete"] + edit_distance_bad(x, y[1:], cost))

    # We want the way that returns the minimum
    return min(costs)


def print_mat(m):
    for r in m:
        print(r)


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

    # print_mat(R)

    # Let's do this right!
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

    # print_mat(R)

    return R[m-1][n-1]


if __name__ == '__main__':

    # print(edit_distance("ab", "acdab", COST))
    # print(edit_distance_bad("ab", "acdab", COST))

    # print(edit_distance("aba", "aaa", COST))
    # print(edit_distance_bad("aba", "aaa", COST))

    # print(edit_distance("aaa", "abc", COST))
    # print(edit_distance_bad("aaa", "abc", COST))

    # print(edit_distance("aaa", "aab", COST))
    # print(edit_distance_bad("aaa", "aab", COST))

    # print(edit_distance("aaa", "aaa", COST))
    # print(edit_distance_bad("aaa", "aaa", COST))

    print(edit_distance("kitten", "sitting", COST))
    print(edit_distance_bad("kitten", "sitting", COST))
