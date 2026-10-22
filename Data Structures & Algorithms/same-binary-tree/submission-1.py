# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def dfs(p, q):
            nonlocal res
            if (not p and q) or (not q and p):
                res = False
                return
            
            if (p and q) and (p.val != q.val):
                res = False
                return

            if p and q:
                left = dfs(p.left, q.left)
                right = dfs(p.right, q.right)
        
        dfs(p, q)
        return res
        

