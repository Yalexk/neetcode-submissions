class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q:
            row, col, i = q.popleft()
            for x, y in directions:
                nbr, nbc = row + x, col + y

                if not (nbr >= ROWS or nbc >= COLS or nbr < 0 or nbc < 0 or grid[nbr][nbc] <= 0):
                    if i + 1 < grid[nbr][nbc]:
                        grid[nbr][nbc] = i + 1
                        q.append((nbr, nbc, i + 1))
        
        return
            