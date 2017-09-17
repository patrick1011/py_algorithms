"""
Derived from https://www.youtube.com/watch?v=GTJr8OvyEVQ

"""


def kmp(text, pattern):
    shift_mapper = compute_shift_mapper(pattern)
    i, j, = 0, 0
    while i < len(text):
        if text[i] != pattern[j]:
            if shift_mapper[j - 1] != 0:
                j = shift_mapper[j - 1]
            else:
                i += 1
        else:
            j += 1
            i += 1
            if j == len(pattern):
                return True
    return False


def compute_shift_mapper(pattern):
    shift_mapper = [0 for _ in enumerate(pattern)]
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] != pattern[j]:
            while pattern[i] != pattern[j] and j > 0:
                j = shift_mapper[j - 1]
            if j == 0:
                shift_mapper[i] = 0
            else:
                shift_mapper[i] = j + 1
        else:
            shift_mapper[i] = j + 1
            j += 1
    return shift_mapper

if __name__ == '__main__':
    arr1 = ['a', 'b', 'x', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'y']
    arr2 = ['a', 'b', 'c', 'a', 'b', 'y']
    print(compute_shift_mapper(list('acacabacacabacacac')))
    # print(kmp(arr1, arr2))
