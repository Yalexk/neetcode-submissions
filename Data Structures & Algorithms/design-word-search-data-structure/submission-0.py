class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i == len(word):
                return root.endOfWord

            c = word[i]
            if c != '.' and c not in root.children:
                return False
            
            if c == '.':
                for char, child in root.children.items():
                    res = dfs(child, i + 1)
                    if res: return True
                return False
            else:
                return dfs(root.children[c], i + 1)

        
        return dfs(self.root, 0)
