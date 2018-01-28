"""
http://www.geeksforgeeks.org/find-the-element-that-appears-once/

Find the element that appears only once in the following sequence:
arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
"""
from math import floor

def hash_solution(arr):
    buff_dict = {}
    for i, elem in enumerate(arr):
        if elem in buff_dict:
            buff_dict[elem] += 1
        else:
            buff_dict[elem] = 1
    for _, elem in enumerate(arr):
        if buff_dict[elem] == 1:
            return elem


def sort_sol(arr):
    quick_sort(arr, 0, len(arr) - 1)
    for i in range(len(arr)):
        if i == 0:
            if arr[0] != arr[1]:
                return arr[0]
        elif i == len(arr)-1:
            return arr[len(arr)-1]
        else:
            if (arr[i] != arr[i - 1]) and (arr[i] != arr[i + 1]):
                return arr[i]


def bitwise_sol(arr):
    arr = list(map(to_binary, arr))
    j = 0
    print(arr)
    while j < 5:
        sum_in_place = 0
        for i in range(len(arr)):
            if (val_in_j_place(arr[i], j) != 0):
                sum_in_place += 1
        print(sum_in_place)
        if sum_in_place % 3 != 0:
            min_val = max(arr)
            for i in range(len(arr)):
                if (val_in_j_place(arr[i], j) != 0 and arr[i] < min_val):
                    min_val = arr[i]
            return to_decimal(min_val)
        j += 1



def val_in_j_place(n, j):
    return floor(n / pow(10, j)) % 10


def to_decimal(n):
    if (n == 0):
        return 0
    decimal, i = 0, 0
    while n > 0:
        remainder = n % 2
        n = int((n - remainder) / 10)
        if remainder != 0:
            decimal = decimal + pow(2, i)
        i += 1
    return decimal


def to_binary(n):
    if (n == 0):
        return 0
    binary, i = 0, 1
    while n > 1:
        remainder = n % 2
        n = int((n - remainder) / 2)
        binary = binary + (remainder * i)
        i *= 10
    return binary + i


def quick_sort(arr, l, r):
    if r > l:
        p_index = partition(arr, l, r)
        quick_sort(arr, l, p_index - 1)
        quick_sort(arr, p_index + 1, r)


def partition(arr, l, r):
    i = l - 1
    for j in range(l, r):
        if arr[j] < arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i + 1] = arr[i + 1], arr[r]
    return i + 1

if __name__ == '__main__':
    arr = [12, 1, 12, 3, 12, 1, 1, 14, 3, 3]
    # print(sort_sol(arr))
    # print(hash_solution(arr))
    print(bitwise_sol(arr))
    # print(to_binary(12310))
