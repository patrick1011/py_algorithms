""" INSERTION SORT
    Notes:
        1. Stable
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

if __name__ == "__main__":
    example_input = [5, 1, 4, 2, 8, 7, 5, 2, 3, 4, 5, 6, 6]

    insertion_sort(example_input)

    print(example_input)
