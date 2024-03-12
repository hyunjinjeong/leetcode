class MyStack:

    def __init__(self):
        self.in_q = collections.deque()
        self.out_q = collections.deque()

    def push(self, x: int) -> None:
        self.in_q.append(x)
        while self.out_q:
            self.in_q.append(self.out_q.popleft())
        self.in_q, self.out_q = self.out_q, self.in_q

    def pop(self) -> int:
        return self.out_q.popleft()

    def top(self) -> int:
        return self.out_q[0]

    def empty(self) -> bool:
        return not self.out_q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
