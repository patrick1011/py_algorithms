

def bubble_sort(arr):
    swap = True
    while swap is True:
        swap = False
        for i in range(len(arr)-1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True


if __name__ == "__main__":
    example_input = [5, 1, 4, 2, 8, 7, 5, 2, 3, 4, 5, 6, 6]

    _sorted = bubble_sort(example_input)
