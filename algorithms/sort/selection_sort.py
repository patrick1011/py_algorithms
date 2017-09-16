def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    example_input = [5, 1, 4, 2, 8, 7, 5, 2, 3, 4, 5, 6, 6]

    selection_sort(example_input)

    print(example_input)
