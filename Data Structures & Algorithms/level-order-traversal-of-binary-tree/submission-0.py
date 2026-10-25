# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def getHeight(root):
            if not root:
                return 0
            
            return 1 + max(getHeight(root.left), getHeight(root.right))
        
        height = getHeight(root)

        res = [[] for _ in range(height)]

        def getChildren(node, depth):
            if node is None:
                return

            if node.left: res[depth].append(node.left.val)
            if node.right: res[depth].append(node.right.val)

            getChildren(node.left, depth + 1)
            getChildren(node.right, depth + 1)
        
        if root: 
            res[0] = [root.val]
            getChildren(root, 1)

        return res

