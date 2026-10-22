# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while cur1 or cur2:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0
            plus = v1 + v2 + carry
            if plus >= 10:
                carry = 1
                cur.next = ListNode(plus - 10)
            else:    
                carry = 0  
                cur.next = ListNode(plus)
            
            cur = cur.next
            if cur1: cur1 = cur1.next 
            if cur2: cur2 = cur2.next 
        
        if carry == 1:
            cur.next = ListNode(1)
        
        return dummy.next

            
