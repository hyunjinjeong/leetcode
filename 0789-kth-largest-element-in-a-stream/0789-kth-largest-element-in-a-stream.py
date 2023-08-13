class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # max heap, min heap을 같이 쓰면..?
        # min heap 원소 개수를 k개, max heap은 len(nums) - k개
        # min heap에다가 더 큰 원소들을 넣고 max heap에는 작은 원소들 넣으면..
        # min heap의 [0]이 k번째.

        # 먼저 max heap에다가 다 넣고, min heap으로 k개를 빼가면 됨
        self.min_heap = []
        self.max_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.max_heap, -1 * num)
        
        # init 시점에는 갯수가 k가 안 될 수가 있어서... min heap으로 옮기는 건 add에서.

    def add(self, val: int) -> int:
        while len(self.min_heap) < self.k and self.max_heap:
            num = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)

        # min heap 크기가 k일 때는 min heap에서 원소를 빼서 max heap으로 옮긴 다음 해야 할 듯?
        if len(self.min_heap) == self.k:
            tmp_min = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * tmp_min)

        num = -1 * heapq.heappushpop(self.max_heap, -1 * val)
        heapq.heappush(self.min_heap, num)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)