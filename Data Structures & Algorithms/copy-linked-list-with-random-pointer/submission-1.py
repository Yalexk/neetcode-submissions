"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = Node(0)
        copyCurr = copy

        o2c = {} # original to copy

        curr = head
        i = 0
        while curr:
            copyCurr.next = Node(curr.val)
            o2c[curr] = copyCurr.next
            curr = curr.next
            copyCurr = copyCurr.next
            i += 1


        # go through and use lookup to reference back to copy
        curr, copyCurr = head, copy.next
        while curr:
            if curr.random is None:
                copyCurr.random = None
            else:
                copyCurr.random = o2c[curr.random]
            curr = curr.next
            copyCurr = copyCurr.next

        return copy.next
