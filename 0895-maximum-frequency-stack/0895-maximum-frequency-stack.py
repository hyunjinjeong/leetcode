class FreqStack:

    def __init__(self):
        # heap을 써야 할 것 같은데...
        # top에 가까운건 뭘로 판단하지?
        # 걍 push할 때마다 index 넣으면 되지 않나..
        self.heap = []
        self.index = 0
        self.freq = collections.defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.index += 1
        
        # min-heap이니까 negate
        element = (-self.freq[val], -self.index, val)
        heapq.heappush(self.heap, element)

    def pop(self) -> int:
        _freq, _index, val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()