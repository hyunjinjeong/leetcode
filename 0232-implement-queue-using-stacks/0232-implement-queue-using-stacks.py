class MyQueue:

    def __init__(self):
        self._in_stack = []
        self._out_stack = []

    def push(self, x: int) -> None:
        while self._out_stack:
            self._in_stack.append(self._out_stack.pop())
        self._in_stack.append(x)

    def pop(self) -> int:
        while self._in_stack:
            self._out_stack.append(self._in_stack.pop())
        return self._out_stack.pop()

    def peek(self) -> int:
        while self._in_stack:
            self._out_stack.append(self._in_stack.pop())
        
        return self._out_stack[-1]

    def empty(self) -> bool:
        return not self._in_stack and not self._out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()