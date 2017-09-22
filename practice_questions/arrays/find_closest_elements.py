from math import floor, ceil


def findClosestElements(arr, k, x):
    last_index = len(arr) - 1
    closest_index = binary_search(arr, 0, last_index, x)
    print(closest_index)
    if closest_index < ceil(k / 2):
        l_bound = 0
        r_bound = k - 1
    elif closest_index + floor(k / 2) > last_index:
        r_bound = last_index
        l_bound = r_bound - k + 1
    else:
        l_bound = closest_index - floor(k / 2)
        r_bound = l_bound + k - 1
        print(l_bound, r_bound, closest_index)
    return arr[l_bound: r_bound + 1]


def binary_search(arr, l, r, key):
    if l < r:
        m = floor((l + r) / 2)
        if key == arr[m]:
            return m
        if key < arr[m]:
            return binary_search(arr, l, m - 1, key)
        return binary_search(arr, m + 1, r, key)
    return l

if __name__ == "__main__":
    _input = [0, 1, 1, 1, 2, 3, 6, 7, 8, 9]
    print(findClosestElements(_input, 9, 4))
