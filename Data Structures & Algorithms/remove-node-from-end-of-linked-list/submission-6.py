# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use offset pointers
        first, second = head, head

        for i in range(n):
            second = second.next
        

        prev = None
        while second:
            prev = first
            first = first.next
            second = second.next

        if prev: 
            prev.next = first.next
            return head
        else:
            return head.next

        
