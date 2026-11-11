class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if ((r, c) in seen or
            r < 0 or c < 0 or
            r >= ROWS or c >= COLS):
                return False
            
            if grid[r][c] == "0":
                return False
            
            seen.add((r,c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return True


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c): res += 1
        
        return res