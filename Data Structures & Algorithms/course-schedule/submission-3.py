class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodeMap = {i: Node(i) for i in range(numCourses)}

        # Courses with no prerequisites
        starters = set(range(numCourses))

        # Construct adjacency list
        for course, prereq in prerequisites:
            nodeMap[prereq].nxt.append(nodeMap[course])
            starters.discard(course)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses

        # Returns True if a cycle is detected
        def dfs(node):
            value = node.val

            if state[value] == VISITED:
                return False

            if state[value] == VISITING:
                return True

            state[value] = VISITING

            for nxt in node.nxt:
                if dfs(nxt):
                    return True

            state[value] = VISITED
            return False

        # Explore all courses with no prerequisites
        for starter in starters:
            if dfs(nodeMap[starter]):
                return False

        # Ensure every course was visited
        return all(s == VISITED for s in state)