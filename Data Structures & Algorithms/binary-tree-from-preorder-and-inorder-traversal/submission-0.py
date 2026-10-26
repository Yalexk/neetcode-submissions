# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        self.pre = 0

        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        def dfs(l, r):
            if l > r:
                return None
            
            val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(val)
            mid = inorderMap[val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            
            return root

        return dfs(0, len(inorder) - 1)
        