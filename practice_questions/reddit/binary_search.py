from math import floor


def binary_search(arr, l, r, k):
    if r >= l:
        mid = floor((l + r) / 2)
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return binary_search(arr, l, mid - 1, k)
        else:
            return binary_search(arr, mid + 1, r, k)


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 8, 10, 13, 15, 17, 21, 27]
    print(binary_search(arr1, 0, len(arr1) - 1, 27))
