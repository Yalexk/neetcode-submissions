class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur = [list('.' * n) for _ in range(n)]
        cols = set()
        posDiag = set()
        negDiag = set()

        def dfs(r):
            # we can place one queen on each row
            if r == n:
                copy = []
                for i in range(n):
                    copy.append("".join(cur[i]))
                res.append(copy)
                return
            
            for c in range(n):
                # see if we can place a queen
                if (c not in cols and (r + c) not in posDiag and (r - c) not in negDiag):
                    cur[r][c] = 'Q'
                    cols.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)

                    dfs(r + 1)

                    cur[r][c] = '.'
                    cols.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
        
        dfs(0)

        return res