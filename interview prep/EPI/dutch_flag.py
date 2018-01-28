def dfp(arr, p_index):
    arr[len(arr) - 1], arr[p_index] = arr[p_index], arr[len(arr) - 1]
    k, j, pivot = -1, -1, arr[len(arr) - 1]
    for i in range(len(arr)):
        if arr[i] == pivot:
            k += 1
            arr[k], arr[i] = arr[i], arr[k]
        elif arr[i] < pivot:
            k += 1
            arr[k], arr[i] = arr[i], arr[k]
            j += 1
            arr[j], arr[k] = arr[k], arr[j]


test1 = [1, 6, 7, 4, 5, 7, 9, 1, 4, 5, 3, 7, 4, 7, 9, 10]
dfp(test1, 3)
print(test1)
