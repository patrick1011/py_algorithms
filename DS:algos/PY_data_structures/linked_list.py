class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sortedInsert(self, new_node):
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while(current.next is not None and
                    current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def search(self, val):
        current = self.head
        while current is not None:
            if current.data == val:
                return current
            current = current.next
        return -1

    #TRIAL NOT TESTED!!
    def getHead(self):
        return self.head

    def remove(self, node):
        if not isinstance(node, Node):
            raise KeyError('that hash key does not exist')
        if node.next is None:
            current = self.head
            if current.next is None:
                self.head = None
                return
            while current is not None:
                if current.next.next is None:
                    current.next = None
                    return node
                current = current.next
            return -1
        else:
            node.data = node.next.data
            node.next = node.next.next

    def __repr__(self):
        if self.head is None:
            return 'empty'
        temp = self.head
        res = []
        while(temp):
            res.append(temp.data)
            temp = temp.next
        return ' '.join(map(str, res))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    # llist = SinglyLinkedList()
    # llist.sortedInsert(Node(10))
    # llist.sortedInsert(Node(7))
    # llist.sortedInsert(Node(31))
    # llist.sortedInsert(Node(14))
    # llist.sortedInsert(Node(9))
    # llist.push(Node(1))
    # llist.push(Node(3))
    # llist.push(Node(4))
    # llist.push(Node(11))
    # llist.remove(llist.search(31))

    llist2 = SinglyLinkedList()
    print(llist2)
    llist2.push(Node(1))
    print(llist2)
    llist2.remove(llist2.search(1))
    print(llist2)
