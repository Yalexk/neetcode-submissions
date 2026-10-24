# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, p, q): # return true if subtree contains p or q
            if root is None:
                return False
            
            if root == p or root == q:
                return True
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            return left or right

        if root is None: # base case
            return

        left = dfs(root.left, p, q)
        right = dfs(root.right, p, q)

        if left and right: 
            return root 
        
        if (left or right) and (root == p or root == q):
            return root

        if left: 
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

