class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        root = TrieNode()

        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.end = True

        res = []
        def dfs(node, r, c, word):
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            (r, c) in path or
            board[r][c] not in node.children):
                return
            
            char = board[r][c]
            path.add((r, c))
            node = node.children[char]
            word.append(char)

            if node.end:
                res.append("".join(word))
                node.end = False

            dfs(node, r + 1, c, word) 
            dfs(node, r - 1, c, word)
            dfs(node, r, c + 1, word)
            dfs(node, r, c - 1, word)

            path.remove((r,c))
            word.pop()

            return

        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c, [])

        return res
            
    
    

     
        

