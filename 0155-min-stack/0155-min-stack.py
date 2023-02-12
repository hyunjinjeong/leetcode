class MinStack:

    def __init__(self):
        self._stack = []
        
    def push(self, val: int) -> None:
        # tuple: (val, curr_min)
        if not self._stack:
            self._stack.append((val, val))
        else:
            self._stack.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()