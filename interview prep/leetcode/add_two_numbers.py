from math import floor

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, x):
        x.next = self.head
        self.head = x

    def getHead(self):
        return self.head


def sol(l1, l2):
    cur1 = l1
    cur2 = l2

    carry = 0
    out = LinkedList()
    while cur1 or cur2 is not None:
        total = cur1.val + cur2.val + carry
        carry = floor(total/10)
        digit = total % 10
        print(cur1.val, cur2.val, total, digit)
        out.push(ListNode(digit))
        cur1 = cur1.next
        cur2 = cur2.next
    return out


if __name__ == '__main__':
    l1 = LinkedList()
    l1.push(ListNode(3))
    l1.push(ListNode(4))
    l1.push(ListNode(2))

    l2 = LinkedList()
    l2.push(ListNode(4))
    l2.push(ListNode(6))
    l2.push(ListNode(5))

    out = sol(l1.getHead(), l2.getHead())
    print(out.getHead())
