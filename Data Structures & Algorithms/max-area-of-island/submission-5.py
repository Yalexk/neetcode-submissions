class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS solution
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0 

        q = collections.deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def bfs(r, c):
            q = collections.deque([(r, c)])
            seen.add((r, c))
            area = 0

            while q:
                r, c = q.popleft()
                area += 1

                for direction in directions:
                    nbr, nbc = r + direction[0], c + direction[1]

                    if (nbr >= ROWS or nbc >= COLS or
                        nbr < 0 or nbc < 0 or
                        (nbr, nbc) in seen or 
                        grid[nbr][nbc] == 0):
                        continue
                    
                    seen.add((nbr, nbc))
                    q.append((nbr, nbc))
            
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in seen:
                    res = max(bfs(i, j), res)
        
        
        return res