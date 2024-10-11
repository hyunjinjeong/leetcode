class StockSpanner:

    def __init__(self):
        # 현재 가격보다 높은 가격의 날을 알아야 함
        # monotonic stack이면 될 듯? decreasing으로 가야 하나
        self.day = 0
        self.stack = []

    def next(self, price: int) -> int:
        self.day += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        last_day = self.stack[-1][1] if self.stack else 0
        self.stack.append((price, self.day))
        
        return self.day - last_day

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)