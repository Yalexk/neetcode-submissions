class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        oq, nq = collections.deque(), collections.deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    oq.append((r, c))
        
        time = 0
        while True:
            while oq:
                r, c = oq.popleft()

                for rdir, cdir in directions:
                    nbr, nbc = r + rdir, c + cdir

                    if (nbr >= ROWS or nbc >= COLS or 
                        nbr < 0 or nbc < 0 or
                        grid[nbr][nbc] != 1):
                        continue
                    
                    grid[nbr][nbc] = 2
                    nq.append((nbr, nbc))

            if not nq:
                break

            time += 1

            while nq:
                oq.append(nq.popleft())
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return time
        




