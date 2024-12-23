class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.history_length = 1
        self.index = 0
        
    def visit(self, url: str) -> None:
        if self.index == len(self.history) - 1:
            self.history.append(url)
        else:
            self.history[self.index + 1] = url
        self.index += 1
        self.history_length = self.index + 1

    def back(self, steps: int) -> str:
        self.index = max(self.index - steps, 0)
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(self.index + steps, self.history_length - 1)
        return self.history[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)