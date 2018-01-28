from math import floor

""" MERGE SORT
    Notes:
        1. Stable.
"""

def merge_sort(arr, l, r):
    if r > l:
        m = floor((l + r) / 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    l_arr = arr[l:m + 1]
    r_arr = arr[m + 1:r + 1]
    l_index, r_index = 0, 0
    for i in range(l, r + 1):
        if l_index == m - l + 1:
            arr[i: r + 1] = r_arr[r_index:]
            break
        if r_index == r - m:
            arr[i: r + 1] = l_arr[l_index:]
            break
        if l_arr[l_index] < r_arr[r_index]:
            arr[i] = l_arr[l_index]
            l_index += 1
        else:
            arr[i] = r_arr[r_index]
            r_index += 1


if __name__ == "__main__":
    example_input = [5, 1, 4, 2, 8, 7, 5, 2, 3, 4, 5, 6, 6]

    merge_sort(example_input, 0, len(example_input) - 1)

    print(example_input)
