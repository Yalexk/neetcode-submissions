# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        # get the height of a tree
        def dfs(cur):
            if cur is None:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)

            nonlocal ans
            if abs(left - right) > 1:
                ans = False

            return max(left, right) + 1
        
        dfs(root)
        return ans
