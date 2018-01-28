""" HEAP
    Notes
    1.  A complete binary tree (each node has up to 2 nodes).
    2.  Get max in O(1)
    3.  Insert in O(log(n))
    4.  Extract max in O(log(n))
    5.  Built in O(nlog(n))
"""

import copy

from math import floor


class MaxHeap:
    def __init__(self, arr):
        self.h = copy.deepcopy(arr)
        self.arr_size = len(arr)
        self.h_size = len(arr)
        for i in range(self.h_size, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.h_size and self.h[i] < self.h[l]:
            largest = l
        if r < self.h_size and self.h[largest] < self.h[r]:
            largest = r
        if largest != i:
            temp = self.h[i]
            self.h[i] = self.h[largest]
            self.h[largest] = temp
            self.max_heapify(largest)

    def get_max(self):
        return(self.h[0])

    def increase_key(self, i, k):
        self.h[i] = k
        while (i > 0) and self.h[floor((i - 1)/2)] < self.h[i]:
            temp = self.h[i]
            self.h[i] = self.h[floor((i - 1)/2)]
            self.h[floor((i - 1)/2)] = temp
            i = floor((i - 1)/2)

    def insert(self, k):
        if self.h_size < self.arr_size:
            self.h_size += 1
            self.increase_key(self.h_size - 1, k)
        else:
            self.arr_size += 1
            self.h_size += 1
            self.h.append(None)
            self.increase_key(self.h_size - 1, k)

    def extract_max(self):
        self.h_size -= 1
        self.h[0], self.h[self.h_size] = self.h[self.h_size], self.h[0]
        self.max_heapify(0)
        return self.h[self.h_size]

    def __repr__(self):
        return str(self.h[0:self.h_size])

if __name__ == "__main__":
    arr = [3, 2, 6, 8, 1, 7, 11, 14, 3, 2, 1]
    max_heap = MaxHeap(arr)
    print(max_heap)
    max_heap.increase_key(8, 20)
    print(max_heap)
    max_heap.insert(12)
    print(max_heap)
    max_heap.extract_max()
    print(max_heap)
