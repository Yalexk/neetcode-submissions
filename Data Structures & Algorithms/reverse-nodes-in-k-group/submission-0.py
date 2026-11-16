# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            s1 = prev_group.next
            # Look ahead k nodes
            cur = s1
            i = 0
            while cur and i < k:
                cur = cur.next
                i += 1

            if i < k:
                break

            s2 = cur
        
            # Reverse group
            cur = s1
            prev = s2
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # Reconnect
            prev_group.next = prev
            prev_group = s1
        
        return dummy.next


