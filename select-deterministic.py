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


def median_of_5(arr):
    """Return median of a group of atmost 5 integers."""
    return sorted(arr)[len(arr)//2]


def median_of_medians(arr, beg, end):
    """
    Find an approx median of arr[beg:end].

    This is then used as a pivot selection strategy in deterministic select

    This is NOT inplace as it creates a new list to store medians of subgroups

    CLRS/Wikipedia have an algorithm that doesn't create a new list but are
    a tad bit confusing.

    https://en.wikipedia.org/wiki/Median_of_medians
    """
    # For less than 5 integers, just return median
    if end - beg < 5:
        return median_of_5(arr)

    # Find medians of 5-integer-subgroups
    medians = []
    for grp_beg in range(beg, end, 5):
        grp_end = min(grp_beg+5, end+1)
        medians.append(median_of_5(arr[grp_beg:grp_end]))

    # Compute median of n/5 medians-of-5
    return select(medians, 0, len(medians)-1, len(medians)//2)


def select(arr, beg, end, k):
    """Return the k-th smallest integer in arr[beg:end]."""

    # If the list has only 1 integer
    if beg == end:
        return arr[beg]

    # Selection with median-of-medians pivot selection
    pvt = median_of_medians(arr, beg, end)
    # NOTE: This assumes that arr has unique integers
    pvt_idx = arr.index(pvt)
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
