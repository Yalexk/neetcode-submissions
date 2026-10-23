class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hmap = {} # maps key to address

        # left is least recent,
        # right is most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.insert(self.hmap[key])
            return self.hmap[key].val
        return -1
        
    # remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])

        if len(self.hmap) > self.cap:
            # remove the least recently used
            lru = self.left.next
            self.remove(lru)
            del self.hmap[lru.key]
            
        


