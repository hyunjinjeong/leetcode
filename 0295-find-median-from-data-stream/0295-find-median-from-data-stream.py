class MedianFinder:
    # min_heap과 max_heap을 둘 다 써서 구현...
    # min_heap은 right half, max_heap은 left half
    # 빼고 넣고 반복하면 min_heap은 큰 원소 n개가 남고 max_heap은 작은 원소 n개
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # 홀수개면 1개는 min_heap으로 넣도록.
        heapq.heappush(self.max_heap, -1 * num)
        heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap) + 1: # 차이가 2개 이상 벌어지면.. 즉 기존에 min_heap이 1개 더 많았던거
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -1 * self.max_heap[0]) / 2
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()