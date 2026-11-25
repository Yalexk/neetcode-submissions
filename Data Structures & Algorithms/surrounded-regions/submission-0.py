class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(r, c):
            if (r >= ROWS or c >= COLS or 
                r < 0 or c < 0 or 
                (r, c) in visited or
                board[r][c] == 'X'):
                return
            
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                    if (r == 0 or c == 0 or
                        r == ROWS - 1 or c == COLS - 1):
                            dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
        
        return