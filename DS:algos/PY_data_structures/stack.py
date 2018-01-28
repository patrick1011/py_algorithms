""" STACK
    Time Complexity:
        Access: O(n)
        Search: O(n) unsorted or O(log(n)) if sorted
        Insertion: O(1)
        Deletion: O(1)
        All above same for average (theta) case
    Used:
        1.  Balancing of symbols (compiler).
        2.  Back/Forwards.
"""


class Stack:
    def __init__(self):
        self.__storage = []

    def isEmpty(self):
        return len(self.__storage) == 0

    def push(self, val):
        self.__storage.append(val)

    def pop(self):
        if self.isEmpty():
            raise ValueError('Cannot pop empty')
        return self.__storage.pop()

    def top(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        return self.__storage[len(self.__storage) - 1]

    def __repr__(self):
        return str(self.__storage)


if __name__ == "__main__":
    new_stack = Stack()
    print(new_stack)
    new_stack.pop()
    print(new_stack)
