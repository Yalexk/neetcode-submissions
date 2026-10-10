# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse the second half of the the nodes, then combine them
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
        
        half = (n + 1) // 2

        # find the halfway point
        curr = head
        for _ in range(half - 1):
            curr = curr.next
        
        second = curr.next
        curr.next = None

        # reverse the second half
        curr = second
        prev = None
        while curr:
            n = curr.next # next node
            curr.next = prev
            prev = curr
            curr = n
        
        # merge
        first, rev = head, prev
        while rev:
            # print(forHead.val)
            fNext, rNext = first.next, rev.next
            first.next = rev
            rev.next = fNext
            rev = rNext
            first = fNext

        return None
