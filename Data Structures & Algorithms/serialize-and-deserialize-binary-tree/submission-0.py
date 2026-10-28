# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # pre order traversal, delimited by a ";"
        res = ""
        def dfs(root):
            nonlocal res
            if not root:
                res += "N" + ","
                return

            res += str(root.val) + ","

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        # print(res.strip(","))
        return res.strip(",")



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # represent it as a delimited string using dfs
        # 1,2,N,N,3,4,N,N,5,N,N
        data = data.split(',')

        i = 0
        def dfs():
            nonlocal i
            value = data[i]
            i += 1

            if value == 'N': return None
            
            node = TreeNode(int(data[i - 1]))
            node.left = dfs()
            node.right = dfs()
        
            return node

        return dfs()
