"""
http://www.geeksforgeeks.org/find-the-maximum-repeating-number-in-ok-time/

Got first time, take homes are range goes to len - 1.
"""

def solution(arr):
    count_len = max(arr) - min(arr) + 1
    count_arr = [0 for _ in range(count_len)]
    for _, elem in enumerate(arr):
        count_arr[elem] += 1
    max_count, max_count_index = 0, 0
    for i, elem in enumerate(count_arr):
        if elem > max_count:
            max_count = elem
            max_count_index = i
    print(count_arr)
    return max_count_index

arr = [1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3]
print(solution(arr))
