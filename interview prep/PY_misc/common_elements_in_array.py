def common_elements_in_sorted_arrays(arr1, arr2):
    sol = []
    i, j, = 0, 0
    while (i < len(arr1)) and (j < len(arr2)):
        if arr1[i] == arr2[j]:
            sol.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return sol


def count_sort(arr):
    count_len = max(arr) + 1
    count_arr = [0 for _ in range(count_len)]
    out = [None for i in range(len(arr))]

    for i in range(len(arr)):
        count_arr[arr[i]] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr)):
        out[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    return out


def sol(arr1, arr2):
    arr1 = count_sort(arr1)
    arr2 = count_sort(arr2)
    return common_elements_in_sorted_arrays(arr1, arr2)

if __name__ == '__main__':
    arr1 = [15, 7, 13, 9, 1, 9]
    arr2 = [2, 6, 7, 13, 15, 18]
    print(sol(arr1, arr2))
