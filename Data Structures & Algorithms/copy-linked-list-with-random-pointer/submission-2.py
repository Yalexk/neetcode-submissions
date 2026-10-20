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
        o2c = {None : None} # original to copy
        cur = head
        while cur:
            copy = Node(cur.val)
            o2c[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = o2c[cur]
            copy.next = o2c[cur.next]
            copy.random = o2c[cur.random]
            cur = cur.next
        
        return o2c[head]
        
