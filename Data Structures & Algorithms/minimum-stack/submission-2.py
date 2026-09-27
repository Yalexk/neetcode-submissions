class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        # have the stack and a minstack
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
            # -2 -2 -3 -3 (-3)
            # -2 -2 -3 (-3)
            # 5 2 1 
        

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()
        
        return popped


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
