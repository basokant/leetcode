from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head

        for _ in range(n):
            right = right.next if right else None

        prev = None
        while left and right:
            prev = left
            left = left.next
            right = right.next

        if prev and left:
            prev.next = left.next

        if head and left == head:
            head = head.next

        return head
