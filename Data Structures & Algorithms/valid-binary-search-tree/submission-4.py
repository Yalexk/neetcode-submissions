# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        seen = set()
        def dfs(node, lo, hi):
            if not node:
                return True
            
            if node.val in seen:
                return False
            seen.add(node.val)
            
            if node.val < lo or node.val > hi:
                return False
            
            left = dfs(node.left, lo, node.val)
            right = dfs(node.right, node.val, hi)

            return left and right
        
        return dfs(root, float("-inf"), float("inf"))
        



