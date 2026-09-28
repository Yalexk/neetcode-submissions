class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 4 13 5 / +
        # 4 + (13 / 5)
        stack = []
        operators = "+-/*"
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                curr = stack.pop()
                prev = stack.pop()
                # print(f"stack: {stack}, operation: {token}")
                match token:
                    case "+":
                        stack.append(curr + prev)
                    case "-":
                        stack.append(prev - curr) 
                    case "/":
                        stack.append(int(prev / curr))
                    case "*":
                        stack.append(prev * curr)
        
        return stack[-1]

