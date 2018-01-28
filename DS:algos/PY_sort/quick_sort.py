""" QUICK SORT
    Notes:
        1. Not stable.
"""


def quick_sort(arr, l, r):
    if r > l:
        p_index = partition(arr, l, r)
        quick_sort(arr, l, p_index - 1)
        quick_sort(arr, p_index + 1, r)


def partition(arr, l, r):
    i = l - 1
    for j in range(l, r):
        if arr[j] <= arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i + 1] = arr[i + 1], arr[r]
    return i + 1

if __name__ == "__main__":
    example_input = [5, 1, 4, 2, 8, 7, 5, 2, 3, 4, 5, 6, 6]
    quick_sort(example_input, 0, len(example_input) - 1)

    print(example_input)
