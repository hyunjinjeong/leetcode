class BrowserHistory:

    def __init__(self, homepage: str):
        # 정직하게 stack에 다 넣으면?
        # visit만 하고 back만 찾을 땐 쉬움. 근데 뒤로 간 상태에서 visit을 하면?
        # O(N)만큼의 삭제 시간이 필요.
        self.arr = [homepage]
        self.index = 0
        
    def visit(self, url: str) -> None:
        if self.index < len(self.arr) - 1:
            self.arr = self.arr[:self.index + 1]

        self.arr.append(url)
        self.index = len(self.arr) - 1

    def back(self, steps: int) -> str:
        self.index = max(self.index - steps, 0)
        return self.arr[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(self.index + steps, len(self.arr) - 1)
        return self.arr[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)