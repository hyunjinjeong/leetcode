class StockSpanner:

    def __init__(self):
        # 현재 가격보다 높은 가격의 날을 알아야 함
        # monotonic stack이면 될 듯? decreasing으로 가야 하나
        self.stack = []

    def next(self, price: int) -> int:
        # 이전 결과를 재활용할 수 있구나
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
    
        self.stack.append((price, res))    
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)