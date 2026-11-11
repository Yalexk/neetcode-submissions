"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge cases
        if node is None:
            return None

        
        keymap = {} # hash map which maps values to copies
        visit = set()
        copy = Node(node.val, None)
        cur, copyCur = node, copy

        def dfs(node, copy):
            visit.add(node.val)
            keymap[node.val] = copy
            for nb in node.neighbors:
                nbCopy = None
                if nb.val in keymap.keys():
                    nbCopy = keymap[nb.val]
                    copy.neighbors.append(nbCopy)
                else:
                    nbCopy = Node(nb.val)
                    copy.neighbors.append(nbCopy)
                                
                if nb.val not in visit:
                    dfs(nb, nbCopy)
        
        dfs(cur, copyCur)
        return copy