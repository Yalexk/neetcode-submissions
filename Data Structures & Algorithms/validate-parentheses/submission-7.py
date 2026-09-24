class Solution:
    def isValid(self, s: str) -> bool:
        # push to a stack when we encounter an open
        # pop when we encounter a close, if its not the same, False

        opens = ['(', '{', '[']
        closes = [')', '}', ']']
        stack = []

        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                if not stack: return False
                oc = stack.pop() + c
                if oc == '()' or oc == '[]' or oc == '{}':
                    continue
                return False

        if not stack: return True

        return False
        