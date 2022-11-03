class MyQueue:
    
    def __init__(self):
        self._in_stack = []
        self._out_stack = []
    
#     # 1. push는 O(n), pop은 O(1) 버전
#     def push(self, x: int) -> None:
#         while self._out_stack:
#             self._in_stack.append(self._out_stack.pop())
#         self._in_stack.append(x)
#         while self._in_stack:
#             self._out_stack.append(self._in_stack.pop())

#     def pop(self) -> int:
#         return self._out_stack.pop()

#     def peek(self) -> int:
#         return self._out_stack[-1]

#     def empty(self) -> bool:
#         return not self._in_stack and not self._out_stack
    # 2. push는 O(1), pop은 O(N) 버전
    def push(self, x: int) -> None:
        self._in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self._out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self._out_stack[-1]
    
    def _move(self):
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())
        
    def empty(self) -> bool:
        return not self._in_stack and not self._out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()