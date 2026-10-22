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
        while cur1 and cur2:
            plus = cur1.val + cur2.val + carry
            if plus >= 10:
                carry = 1
                cur.next = ListNode(plus - 10)
            else:    
                carry = 0  
                cur.next = ListNode(plus)
            
            cur, cur1, cur2 = cur.next, cur1.next, cur2.next
        
        if not cur1: cur1 = cur2

        while cur1:
            plus = cur1.val + carry
            if plus >= 10:
                carry = 1
                cur.next = ListNode(plus - 10)
            else:
                carry = 0
                cur.next = ListNode(plus)
            cur, cur1 = cur.next, cur1.next
        
        if carry == 1:
            cur.next = ListNode(1)
        
        return dummy.next

            
