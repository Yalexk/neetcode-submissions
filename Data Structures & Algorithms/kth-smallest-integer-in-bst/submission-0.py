# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 1 is smallest
        # n is largest
        # traverse left to right
        count = 0
        res = None
        def dfs(node, k):
            

            nonlocal count
            if node is None:
                return
            # print(count + 1, node.val)
            
            left = dfs(node.left, k)
            count += 1
            if count == k:
                nonlocal res
                res = node.val
            right = dfs(node.right, k)

        
        dfs(root, k)
        return res


            
            
