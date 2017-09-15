from random import randint

import sys
import time

# Count the no. of comparisons in partitioning
comparison_count = 0


def swap(arr, i, j):
    """Inplace swap values in an array."""
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, beg, end, pvt_idx):
    """
    Inplace partition-ing of arr[beg:end] around pivot (arr[pvt_idx]).

    Return the updated index of pivot.
    """

    global comparison_count

    pvt = arr[pvt_idx]

    # Move pivot to the end
    swap(arr, end, pvt_idx)

    # This will store the new index of pivot
    pvt_new_idx = beg

    for idx in range(beg, end):

        # Move values smaller than pivot to the beginning of array
        comparison_count += 1
        if arr[idx] < pvt:
            swap(arr, idx, pvt_new_idx)
            pvt_new_idx += 1

    # Move pivot to new position
    swap(arr, end, pvt_new_idx)

    return pvt_new_idx


# NOTE: This assumes 1 based order statistics
# so minimum is the first order statistic
def select(arr, beg, end, k):
    """
    Return the k-th smallest number in arr[beg:end]
    """

    # If the list has only 1 number
    if beg == end:
        return arr[beg]

    # Selection with randomized pivot selection
    pvt_idx = randint(beg, end)
    pvt_new_idx = partition(arr, beg, end, pvt_idx)

    if k == pvt_new_idx:
        return arr[pvt_new_idx]
    elif k < pvt_new_idx:
        return select(arr, beg, pvt_new_idx - 1, k)
    elif k > pvt_new_idx:
        return select(arr, pvt_new_idx + 1, end, k)


def read_int_file_to_list(filename):
    """Return a list of numbers read from filename."""

    arr = []
    # TODO: Buffered input may increase perf?
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

    times, comparisons = [], []
    for _ in range(0, 10):

        start = time.clock()
        comparison_count = 0

        ans = select(arr, 0, len(arr)-1, k-1)

        end = time.clock()

        times.append(end-start)
        comparisons.append(comparison_count)

    print("Integer with rank %d: %d" % (k, ans))
    print("\n-----\n")

    print("No. of comparisons: %d" % (sum(comparisons) / len(comparisons)))
    print("Time taken (avg of 10 runs): %0.3f sec" % (sum(times) / len(times)))
