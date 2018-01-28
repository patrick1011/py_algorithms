""" QUEUE
    Time Complexity:
        Access: O(n)
        Search: O(n)
        Insertion: O(1)
        Deletion: O(1)
        All above same for average (theta) case
    Used:
        1.  When a resource is shared among multiple
            consumers. Examples include CPU scheduling,
            Disk Scheduling.
"""


class Queue:
    def __init__(self):
        self.__storage = []

    def isEmpty(self):
        return self.__storage == []

    def enqueue(self, item):
        self.__storage.insert(0, item)

    def dequeue(self):
        return self.__storage.pop()

    def size(self):
        return len(self.__storage)

    def __repr__(self):
        return str(self.__storage)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(1)
    queue.enqueue(10)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue)
