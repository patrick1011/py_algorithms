"""
http://www.geeksforgeeks.org/find-the-element-that-appears-once/

Find the element that appears only once in the following sequence:
arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
"""

def sort_sol(arr):
    return quick_sort(arr, 0, len(arr) - 1)


def quick_sort(arr, l, r):
    if r > l:
        p_index = partition(arr, l, r)
        quick_sort(arr, l, p_index - 1)
        quick_sort(arr, p_index + 1, l)


def partition(arr, l, r):
    i = l - 1
    for j in range(l, r):
        if arr[j] < arr[r]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[r], arr[i + 1] = arr[i + 1], arr[r]
    return i + 1

if __name__ == '__main__':
    arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
    print(sort_sol(arr))
