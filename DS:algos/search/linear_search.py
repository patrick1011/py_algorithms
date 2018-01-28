def linear_search(arr, var):
    for i in range(len(arr)):
        if var == arr[i]:
            return i
    return - 1

if __name__ == "__main__":
    example_input = [5, 1, 4, 2, 8, 7, 5, 2, 3, 4, 5, 6, 6]

    a = linear_search(example_input, 41)

    print(a)
