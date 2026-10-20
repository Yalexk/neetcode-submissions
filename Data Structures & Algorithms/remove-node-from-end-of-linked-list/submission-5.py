# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if length == 1:
            return None
        
        stop = length - n
        if stop == 0:
            return head.next
    
        i = 0
        curr, prev = head, None 
        while i < stop:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next

        return head
