class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substrings = [s[0]]

        def checkPalindrome(s):
            mid = len(s) // 2
            first = s[:mid]
            second = None
            if len(s) % 2 == 0:
                second = s[mid:]
                second = second[::-1]
            else:
                second = s[mid + 1:]
                second = second[::-1]
            
            if first == second:
                return True
            
            return False

        def dfs(i):
            if i == len(s):
                if checkPalindrome(substrings[-1]):
                    res.append(substrings.copy())
                return
            
            substrings[-1] += s[i]
            dfs(i + 1)

            substrings[-1] = substrings[-1][:-1]

            # only split if the current is a palindrome
            if checkPalindrome(substrings[-1]):
                substrings.append(s[i])
                dfs(i + 1)
                substrings.pop()
            
            return


        dfs(1)

        return res