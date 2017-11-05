"""Edit Distance between two strings."""

import sys


def edit_distance(x, y, cost):

    # print("%r %r %r" % (x, y, cost))

    m, n = 1 + len(x), 1 + len(y)

    # Use two rows instead of a complete matrix
    prev = [cost["insert"] * j for j in range(n)]

    # Go over each character of strings x & y
    for i in range(1, m):

        curr = []

        for j in range(1, n):

            if j == 1:
                curr.append(cost["delete"] * i)

            # Costs of various ways of making the strings equal
            costs = []

            # Copy is only possible when the characters match
            if x[i-1] == y[j-1]:  # account for 0 based string indexing
                costs.append(cost["copy"] + prev[j-1])

            # Other ways are always possible

            # Replace
            costs.append(cost["replace"] + prev[j-1])

            # Insert
            costs.append(cost["insert"] + prev[j])

            # Delete
            costs.append(cost["delete"] + curr[j-1])

            # We want the way that returns the minimum
            curr.append(min(costs))

        prev = curr

    return curr[n-1]


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: edit-distance.py <filename>")
        exit(1)

    with open(sys.argv[1]) as f:

        lines = list(map(lambda l: l.strip(), f.readlines()))

        if len(lines) % 3 != 1:
            print("Input file should contain 3T + 1 lines:\n"
                  "the first line has number of test cases T\n"
                  "where a single test case has "
                  "line 1: string x\n"
                  "line 2: string y\n"
                  "line 3: cost list in the format <copy>,<insert>,<replace>,<delete>")
            exit(1)

        t = int(lines[0])

        for i in range(0, t):

            x = lines[3*i + 1]
            y = lines[3*i + 2]

            if x and y and not (x.isalnum() and y.isalnum()):
                print("Strings should be alpha-numeric: [a-zA-Z0-9]*")
                exit(1)

            cost_type = ["copy", "insert", "replace", "delete"]
            cost_list = list(map(int, lines[3*i + 3].split(",")))

            if len(cost_list) != 4:
                print("Cost list should have 4 entries separated by ,: \n"
                      "<copy>,<insert>,<replace>,<delete>")
                exit(1)

            cost = dict(zip(cost_type, cost_list))

            ans = edit_distance(x, y, cost)
            print(ans % (10 ** 9 + 7))
