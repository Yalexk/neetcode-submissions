# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def getChildren(node, depth):
            if node is None:
                return

            if depth > len(res):
                res.append([])
            
            res[depth - 1].append(node.val)

            getChildren(node.left, depth + 1)
            getChildren(node.right, depth + 1)
        
        getChildren(root, 1)

        return res

