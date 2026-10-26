class PrefixTree:
    # self.c = String
    # self.children = []

    def __init__(self):
       self.end = False
       self.children = [None] * 26 # array of size 26

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = PrefixTree()
            curr = curr.children[index]
        
        curr.end = True

            

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return False
            
            curr = curr.children[index]
        
        return curr.end and True
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return False
            
            curr = curr.children[index]
        
        return True

        
        