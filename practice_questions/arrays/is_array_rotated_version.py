"""
Given 2 integer arrays, determine of the 2nd array
is a rotated version of the 1st array. Ex. Original
Array A=[1,2,3,5,6,7,8] Rotated Array B=[5,6,7,8,1,2,3]

"""
from algorithms.string_matching.simple_substring_search import simple_substring_search


def solution(arr1, arr2):
    """
        Solution creates arr2arr2 and checks to see if arr1
        is in there.
    """
    if len(arr1) != len(arr2):
        return False

    return simple_substring_search(arr1*2, arr2)


arr1 = [1, 2, 3, 5, 6, 7, 8]
arr2 = [5, 6, 7, 8, 1, 2, 3]

print(solution(arr1, arr2))
