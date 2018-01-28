def simple_substring_search(arr1, arr2):
    """
        O(m * n).
    """
    j, i, last_failed = 0, 0, 0
    while i < len(arr1):
        if (arr1[i] == arr2[j]):
            j += 1
            i += 1
            if j == len(arr2):
                return True
        else:
            last_failed, i = last_failed + 1, last_failed + 1
            j = 0
    return False
