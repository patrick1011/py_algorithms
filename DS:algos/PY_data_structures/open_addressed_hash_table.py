""" HASH TABLE with open addressing:

    To do - go through detailed pros and cons of this and the other.
"""
from math import pow


class HashTable:
    def __init__(self):
        self.m = 11
        self.n = 0
        self.table = [None for x in range(self.m)]

    def insert(self, key):
        i = 0
        while True:
            candidate = self.hash_fn(key, i)
            if self.table[candidate] is None:
                self.table[candidate] = key
                self.n += 1
                break
            i += 1
        if self.n is self.m - 1:
            self.resize_table(self.m * 2)

    def resize_table(self, size_to):
        self.m = size_to
        self.n = 0
        temp_table = self.table
        self.table = [None for x in range(self.m)]
        for elem in temp_table:
            if elem is not None and elem is not'deleted':
                self.insert(elem)

    def hash_fn(self, key, i):
        "Quadratic probing"
        return (key + int(pow(i, 2))) % self.m

    def search(self, key):
        i = 0
        while True:
            candidate = self.hash_fn(key, i)
            if (self.table[candidate] is None):
                raise KeyError('key does not exist')
            if self.table[candidate] is key:
                return candidate
            i += 1

    def delete(self, key):
        index = self.search(key)
        self.table[index] = 'deleted'
        self.n -= 1
        if self.n < (self.m / 4):
            self.resize_table(int(self.m / 2))

    def __repr__(self):
        return str(self.table)

if __name__ == "__main__":
    oa_table = HashTable()
    oa_table.insert(1)
    oa_table.insert(57)
    oa_table.insert(104)
    oa_table.insert(42)
    oa_table.insert(39)
    print(oa_table)
    oa_table.insert(42)
    oa_table.insert(0)
    oa_table.insert(43)
    oa_table.insert(63)
    print(oa_table)
    oa_table.delete(63)
    oa_table.delete(43)
    oa_table.delete(0)
    oa_table.delete(42)
    oa_table.delete(1)
    oa_table.delete(57)
    oa_table.delete(104)
    print(oa_table)
