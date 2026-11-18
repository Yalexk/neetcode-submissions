class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        areas = {}
        ROWS, COLS = len(grid), len(grid[0])
        res = 0 

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in seen or
                grid[r][c] == 0):
                return 0
            
            seen.add((r, c))

            area = (
                dfs(r + 1, c) + 
                dfs(r - 1, c) + 
                dfs(r, c + 1) + 
                dfs(r, c - 1)) + 1
            
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in seen:
                    res = max(dfs(i, j), res)
        
        
        return res