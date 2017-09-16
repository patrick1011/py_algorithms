"""
Derived from https://www.youtube.com/watch?v=GTJr8OvyEVQ

"""


def kmp(text, pattern):
    shift_mapper = compute_shift_mapper([1, 2, 3, 4, 1, 2, 3])
    return shift_mapper


def compute_shift_mapper(pattern):
    shift_mapper = [0 for _ in enumerate(pattern)]
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] != pattern[j]:
            shift_mapper[i] = 0
        else:
            shift_mapper[i] = j + 1
            j += 1
    return shift_mapper

if __name__ == '__main__':
    arr1 = [1, 2, 3, 5, 6, 7, 8]
    arr2 = [5, 6, 7, 8, 1, 2, 3]
    print(kmp(arr1*2, arr2))
