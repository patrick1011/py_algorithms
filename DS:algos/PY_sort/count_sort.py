from data_structures.array import find_max

""" COUNT SORT
    Time Complexity: O(n + maxval) - (can be maxval - minval)
    Space Complexity: O(n + k) - len(out) and len(cum)
    Notes:
        1.  Efficient when k < n.
        2.  Uses partial hashing to count occurence in O(1).
    To determine:
        1.  Parallelizing?
        2.  Stable, online?  <- what do these mean?
        3.  Does it only work with integers?
    Tasks, things to experiment:
        1.  Modify to work on negative integers.
        2.  Reduce time complexity to maxval - minval.
    Other:
        Below looks a bit weird so it works with radix,
        when implementing generally don't include sort_on.
"""


def count_sort(arr, sort_on=lambda x: x):
    maxval = find_max(list(map(sort_on, arr)))
    n = len(arr)

    cum = [0 for _ in range(maxval + 1)]
    out = [None for i in range(n)]

    for _, val in enumerate(arr):
        cum[sort_on(val)] += 1

    for i in range(1, len(cum)):
        cum[i] += cum[i - 1]

    # reverse for radix
    for val in reversed(arr):
        out[cum[sort_on(val)] - 1] = val
        cum[sort_on(val)] -= 1
    return out

if __name__ == "__main__":
    arr = [10, 21, 42, 18, 93]
    print(arr)
