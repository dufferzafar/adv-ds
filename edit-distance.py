"""Edit Distance between two strings."""

import sys


def edit_distance(x, y, cost):

    # print("%r %r %r" % (x, y, cost))

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


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: edit-distance.py <filename>")
        exit(1)

    with open(sys.argv[1]) as f:

        lines = map(lambda l: l.strip(), f.readlines())

        if len(lines) != 3:
            print("Input file should contain 3 lines:\n"
                  "line 1: string x\n"
                  "line 2: string y\n"
                  "line 3: cost list in the format <copy>,<insert>,<replace>,<delete>")
            exit(1)

        x = lines[0]
        y = lines[1]

        if not (x.isalnum() and y.isalnum()):
            print("Strings should be alpha-numeric.")
            exit(1)

        cost_type = ["copy", "insert", "replace", "delete"]
        cost_list = map(int, lines[2].split(","))

        if len(cost_list) != 4:
            print("Cost list should have 4 entries separated by ,: \n"
                  "<copy>,<insert>,<replace>,<delete>")
            exit(1)

        cost = dict(zip(cost_type, cost_list))

        print(edit_distance(x, y, cost))
