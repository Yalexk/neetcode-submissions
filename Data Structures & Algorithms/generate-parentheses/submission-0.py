class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = ['(']
        res = []

        # track depth and remaining
        def dfs(openb, closeb):
            if len(cur) == 2 * n:
                res.append(''.join(cur.copy()))
                return
            
            if openb < n:
                cur.append('(')
                dfs(openb + 1, closeb)
                cur.pop()
            
            if closeb < openb:
                cur.append(')')
                dfs(openb, closeb + 1)
                cur.pop()

        dfs(1, 0)

        return res
