class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # days before it will return to warm
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack: 
                stack.append(i)
                continue
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)

        return result
        # res: [1, 4, 1, 2, 1, 0, 0]
        # stack: [5 28]


        

