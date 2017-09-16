from math import floor

""" BINARY SEARCH
    Time Complexity = T(n) = T(n/2) + O(1) = log(n)
    Notes:
        1. Example of divide and conquer.
"""


def binary_search(arr, l, r, key):
    if r >= l:
        m = floor((l + r) / 2)
        if arr[m] == key:
            return m
        elif arr[m] > key:
            return binary_search(arr, l, m - 1, key)
        return binary_search(arr, m + 1, r, key)
    return - 1

if __name__ == "__main__":
    example_input = [1, 3, 5, 6, 6, 8, 9, 10, 14, 17, 19]
    print(binary_search(example_input, 0, len(example_input) - 1, 19))
