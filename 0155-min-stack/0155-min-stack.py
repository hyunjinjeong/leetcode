class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = None

    def push(self, val: int) -> None:
        self.curr_min = min(val, self.curr_min) if self.curr_min is not None else val
        self.stack.append(Node(val, self.curr_min))

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min = self.stack[-1].curr_min if self.stack else None

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].curr_min
        

class Node:
    
    def __init__(self, val, curr_min):
        self.val = val
        self.curr_min = curr_min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()