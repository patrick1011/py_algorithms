""" HASH TABLE:
    Time Complexity:
        Insert: O(1), Delete: O(1 + m/n), Search: O(1 + m/n)

    Things to do:
        1. Dont double but go to next prime
"""


from data_structures.linked_list import SinglyLinkedList, Node


class HashTable:
    def __init__(self):
        self.m = 5
        self.n = 0
        self.table = [SinglyLinkedList() for x in range(self.m)]

    def insert(self, key):
        index = self.hash_fn(key)
        self.table[index].push(Node(key))
        self.n += 1
        if self.n > self.m:
            self.resize_table(self.m * 2)

    def resize_table(self, size_to):
        self.m = size_to
        self.n = 0
        temp_table = self.table
        self.table = [SinglyLinkedList() for x in range(self.m)]
        for bucket in temp_table:
            node = bucket.head
            while node is not None:
                self.insert(node.data)
                node = node.next

    def hash_fn(self, k):
        return k % self.m

    def delete(self, key):
        index = self.hash_fn(key)
        node = self.table[index].search(key)
        self.table[index].remove(node)
        self.n -= 1
        if self.n < (self.m / 4):
            self.resize_table(int(self.m / 2))

    def __repr__(self):
        return str(self.table)

if __name__ == "__main__":
    ch_table = HashTable()
    ch_table.insert(1)
    ch_table.insert(57)
    ch_table.insert(101)
    ch_table.insert(42)
    print(ch_table)
    ch_table.insert(33)
    ch_table.insert(43)
    ch_table.insert(63)
    print(ch_table)
    ch_table.delete(63)
    ch_table.delete(1)
    ch_table.delete(101)
    ch_table.delete(57)
    ch_table.delete(42)
    print(ch_table)
