class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        areas = {}

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, hr, hc):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in seen or
                grid[r][c] == 0):
                return
            
            seen.add((r, c))
            nonlocal res

            areas[(hr, hc)] = areas.get((hr,hc), 0) + 1

            dfs(r + 1, c, hr, hc)
            dfs(r - 1, c, hr, hc)
            dfs(r, c + 1, hr, hc)
            dfs(r, c - 1, hr, hc)

            return

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in seen:
                    dfs(i, j, i, j)
        
        res = 0
        for area in areas.values():
            res = max(res, area)
        
        return res