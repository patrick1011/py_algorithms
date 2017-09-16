"""
http://www.geeksforgeeks.org/sort-elements-by-frequency/

Print the elements of an array in the decreasing frequency
if 2 numbers have same frequency then print the one which
came first.

Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}

Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}
"""


def ans(arr):
    for i in range(len(arr)):
        arr[i] = [arr[i], i]

    quick_sort(arr, 0, len(arr) - 1, lambda x: x[0])
    count = count_sorted_frequencies(arr)
    quick_sort(count, 0, len(count) - 1, lambda x: x[1])

    l, r = 0, 0
    for i in range(len(count) - 1):
        if count[i + 1][1] != count[i][1]:
            quick_sort(count, l, r, lambda x: x[2])
            l, r = i + 1, i
        r += 1

    out = []
    for i, val in enumerate(count):
        for i in range(val[1]):
            out.append(val[0])
    return out


def count_sorted_frequencies(arr):
    count = []
    prev = None
    j = -1
    for i in range(len(arr)):
        if arr[i][0] == prev:
            count[j][1] += 1
        else:
            # in conventional version would be
            # count.append([arr[i], 1])
            count.append([arr[i][0], 1, arr[i][1]])
            j += 1
        prev = arr[i][0]
    return count


def quick_sort(arr, l, r, sort_on=lambda x: x):
    if r > l:
        p_index = partition(arr, l, r, sort_on)
        quick_sort(arr, l, p_index - 1, sort_on)
        quick_sort(arr, p_index + 1, r, sort_on)


def partition(arr, l, r, sort_on):
    i = l - 1
    for j in range(l, r):
        if sort_on(arr[j]) < sort_on(arr[r]):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i + 1] = arr[i + 1], arr[r]
    return i + 1


if __name__ == "__main__":
    example_input = [3, 3, 2, 5, 2, 8, 5, 6, 8, 8]
    print('in: ', example_input)
    print('out: ', ans(example_input))
