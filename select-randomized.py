from random import randint

import sys


def swap(arr, i, j):
    """Inplace swap values in an array."""
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, beg, end, pvt_idx):
    """
    Inplace partition-ing of arr[beg:end] around pivot (arr[pvt_idx]).

    Return the updated index of pivot.
    """

    pvt = arr[pvt_idx]

    # Move pivot to the end
    swap(arr, end, pvt_idx)

    # This will store the new index of pivot
    pvt_new_idx = beg

    for idx in range(beg, end):

        # Move values smaller than pivot to the beginning of array
        if arr[idx] < pvt:
            swap(arr, idx, pvt_new_idx)
            pvt_new_idx += 1

    # Move pivot to new position
    swap(arr, end, pvt_new_idx)

    return pvt_new_idx


def select(arr, beg, end, k):
    """
    Return the k-th smallest integer in arr[beg:end]
    """

    # If the list has only 1 integer
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
    """Return a list of integers read from filename."""

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

    # NOTE: This assumes 1 based order statistics
    # so minimum is the first order statistic
    ans = select(arr, 0, len(arr)-1, k-1)

    print("Integer with rank %d is: %d" % (k, ans))
