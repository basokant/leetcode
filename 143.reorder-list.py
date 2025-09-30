from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tail = None
        if slow:
            tail = self.reverseList(slow.next)
            slow.next = None

        while head and tail:
            next_head, next_tail = head.next, tail.next
            head.next = tail
            tail.next = next_head
            head, tail = next_head, next_tail
