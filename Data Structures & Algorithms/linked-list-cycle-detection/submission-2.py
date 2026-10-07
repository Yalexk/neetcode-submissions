# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # have a slow pointer and the fast pointer
        # if there is a cycle the fast one will catch up
        slow, fast = head, head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next

            if not fast or not fast.next:
                return False
            
            if slow == fast:
                return True

        return False