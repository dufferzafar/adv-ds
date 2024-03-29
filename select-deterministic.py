import sys
import time

# Count the no. of comparisons in partitioning
comparison_count = 0


def median_of_5(arr):
    """Return median of a group of atmost 5 integers."""
    return sorted(arr)[len(arr)//2]


def select(arr, k):
    """
    Return the k-th smallest integer in arr.

    Reference: https://www.ics.uci.edu/~eppstein/161/960130.html
    """

    global comparison_count

    # For less than 5 numbers, just return answer
    if len(arr) < 5:
        return sorted(arr)[k]

    # Find medians of 5-number-subgroups
    medians = [
        median_of_5(arr[i:i+5])
        for i in range(0, len(arr), 5)
    ]

    # Compute median of n/5 medians-of-5
    median_of_medians = select(medians, (len(medians)-1)//2)

    # Partition arr into 3 parts arround median_of_medians
    lesser, higher, equal = [], [], []

    for num in arr:
        comparison_count += 2
        if num < median_of_medians:
            lesser.append(num)
        elif num > median_of_medians:
            higher.append(num)
        else:
            equal.append(num)

    # Decide which array to recur on
    comparison_count += 2
    if k < len(lesser):
        return select(lesser, k)

    elif k < len(lesser) + len(equal):
        return equal[0]

    else:
        return select(higher, k-len(lesser)-len(equal))


def read_int_file_to_list(filename):
    """Return a list of integers read from filename."""

    arr = []
    with open(filename, "r") as file:
        for line in file:
            if line:
                arr.append(int(line))

    return arr


if __name__ == '__main__':
    arr = read_int_file_to_list(sys.argv[1])

    k = int(sys.argv[2])

    if not (1 <= k <= len(arr)):
        print("k should be in between 1 & %d" % len(arr))
        exit(1)

    # NOTE: This assumes 1 based order statistics
    # so minimum is the first order statistic
    start = time.clock()
    ans = select(arr, k-1)
    end = time.clock()

    print("Integer with rank %d: %d" % (k, ans))
    print("\n-----\n")

    print("No. of comparisons: %d" % comparison_count)
    print("Time taken: %0.3f sec" % (end-start))
