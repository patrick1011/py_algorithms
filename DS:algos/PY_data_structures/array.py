""" ARRAY
Time Complexity:
    Access: O(1)
    Search: O(n)
    Insertion: O(n)
    Deletion: O(n)
    Find min/max: O(n)
    All above same for average (theta) case
"""


def linear_search(arr, var):
    for i in range(len(arr)):
        if var == arr[i]:
            return i
    return - 1


def find_max(arr):
    max_so_far = arr[0]
    for cur in arr:
        if cur > max_so_far:
            max_so_far = cur
    return max_so_far


def reverse(arr, l, r):
    i, j = l, r
    while (i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr
