# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1, length2 = 0, 0
        cur1, cur2 = l1, l2
        
        while cur1:
            length1 += 1
            cur1 = cur1.next
        
        while cur2:
            length2 += 1
            cur2 = cur2.next
        
        # have l1 be the bigger always
        if length1 < length2:
            temp, templength = l1, length1
            l1, length1 = l2, length2
            l2, length2 = temp, templength
        
        cur1, cur2 = l1, l2
        i = 0
        total = 0

        while i < length2:
            total += (10 ** i) * (cur1.val + cur2.val)
            # print(total)
            i += 1
            cur1, cur2 = cur1.next, cur2.next
        
        while i < length1:
            total += (10 ** i) * (cur1.val)
            # print(total)
            i += 1
            cur1 = cur1.next
        
        # print(total)
        dummy = ListNode(0)
        cur = dummy
        for i in range(1, len(str(total)) + 1):
            cur.next = ListNode(int(str(total)[-i]))
            cur = cur.next

        return dummy.next