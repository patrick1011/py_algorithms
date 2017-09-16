from data_structures.linked_list import LinkedList, Node

""" BUCKET SORT
    Time Complexity: O(n)
    Notes:
        1.  Used when input is uniformly distributed over
            a range.
        2.  This implementation does insertion sort as it goes.
        3.  Insertion sorting on average takes O(n) if uniform (CLRS).
    To determine:
        1.  Parallelizing?
        2.  Stable, online?  <- what do these mean?
        3.  When good to use?
"""


def bucket_sort(arr):
    bucket_len = 10
    buckets = [LinkedList() for x in range(bucket_len)]
    for value in arr:
        new_node = Node(value)
        index = int(value * bucket_len)
        buckets[index].sortedInsert(new_node)
    result = []
    for bucket in buckets:
        if bucket.head is not None:
            result.append(bucket)
    return result


if __name__ == "__main__":
    sorted = bucket_sort([0.4, 0.8, 0.2, 0.6, 0.1, 0.5, 0.55, 0.54])
    print(sorted)
