"""
Write a function rotate(ar[], d
that rotates arr[] of size n by d elements.

Do it in:
    1. O(n) time and space.
    2. O(d*n) time and O(1) space.

http://www.geeksforgeeks.org/array-rotation/
"""


def ans_1(arr, d):
    """O(n) time and space."""
    out = [None for i in arr]
    for i in range(len(arr)):
        out[i] = arr[(i - d) % len(arr)]
    return out


def ans_2(arr, d):
    """O(d*n) time and space."""
    for i in range(d):
        temp = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[len(arr) - 1] = temp
    return arr


def ans_3(arr, d):
    """O(n) time, no extra space!"""
    reverse(arr, 0, d - 1)
    reverse(arr, d, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)
    return arr


def reverse(arr, l, r):
    i, j = l, r
    while (i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

if __name__ == "__main__":
    example_input = [3, 3, 2, 5, 2, 8, 5, 6, 8, 8]
    print('Answer 1')
    print('in: ', example_input)
    print('out: ', ans_1(example_input, 2))
    print('Answer 2')
    print('in: ', example_input)
    print('out: ', ans_2(example_input, 8))
    print('Answer 3')
    example_input = [3, 3, 2, 5, 2, 8, 5, 6, 8, 8]
    print('in: ', example_input)
    print('out: ', ans_3(example_input, 8))
