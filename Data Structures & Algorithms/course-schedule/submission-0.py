class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodeMap = {}
        for i in range(numCourses):
            nodeMap[i] = Node(i)
        
        # nodes that have no prereqs
        starters = set([i for i in range(numCourses)])
        
        for course in prerequisites:
            prereq, nxt = course[1], course[0]
            nodeMap[prereq].nxt.append(nodeMap[nxt])
            if nxt in starters: starters.remove(nxt)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        state = [UNVISITED] * numCourses

        # return True if a cycle is detected
        def dfs(node): 
            value = node.val               
            if state[value] == VISITED:
                return False
            
            if state[value] == VISITING:
                return True
            state[value] = VISITING

            for nxt in node.nxt:
                if dfs(nxt): return True
            
            state[value] = VISITED

            return False


        for starter in starters:
            if dfs(nodeMap[starter]): return False
        
        for node in state:
            if node == UNVISITED: return False
        
        return True

        














