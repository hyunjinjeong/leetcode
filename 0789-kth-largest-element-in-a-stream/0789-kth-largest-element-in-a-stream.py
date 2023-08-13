class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # 아 너무 복잡하게 생각했다...
        # 그냥 min heap만 써도 되는 거였음
        # k번째로 큰 원소 -> size가 k인 min heap을 구성하면 알아서 됨. 작은 원소부터 빠져나가니까...

        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)