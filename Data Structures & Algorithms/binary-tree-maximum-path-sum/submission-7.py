# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def dfs(root):
            if root is None:
                return 0

            nonlocal ans
            ans = max(ans, root.val)

            if root.left is None and root.right is None:
                return root.val
            
            left, right = dfs(root.left), dfs(root.right)
            left, right = max(left, 0), max(right, 0)

            # check left only, right only, all
            total = root.val + left + right
            
            ans = max(ans, total)

            return root.val + max(left, right)
        
        dfs(root)
        return ans
        
