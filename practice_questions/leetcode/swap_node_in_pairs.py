"""
    https://leetcode.com/problemset/all/

    Lessons:
        Getting a sense of what to do before coding was efficient (could do more).
        Didn't consider edge cases - write list up front.
        To do next: only start coding when a full solution is in mind.
"""


class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return None
        elif head.next is None:
            return head
        out = head.next
        prev = ListNode(None)
        first = head
        while first and first.next:
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev, first = first, first.next
        return out
