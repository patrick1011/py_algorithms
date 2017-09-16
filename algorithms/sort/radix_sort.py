from algorithms.sort.count_sort import count_sort
from data_structures.array import find_max

""" RADIX SORT
    Time Complexity: O(d*(n + b)) chosse b=n
    Notes:
        1.  Even though O(n) when b=n, quicksort:
            a) Uses hardware caches.
            b) Has smaller constant factors.
        2.  Uses counting sort which has O(n + k) space complexity.
    To determine:
        1.  Parallelizing?
        2.  What does 'every digit takes log2(n) bits' mean?
"""


def radix_sort(arr):
    max = find_max(arr)
    exp = 1
    while max >= exp:
        def exp_digit(x):
            return int((x / exp) % 10)
        arr = count_sort(arr, exp_digit)
        exp *= 10
    return arr

if __name__ == "__main__":
    example_input = [500, 112, 423, 21, 89, 77, 519, 220, 317]
    print(radix_sort(example_input))
