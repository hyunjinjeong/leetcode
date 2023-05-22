class MedianFinder:
    # 오...  max heap과 min heap을 둘 다 쓰는게 포인트였음.
    # max heap은 small half, min heap은 large half.
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [] # small half
        self.min_heap = [] # large half
        

    def addNum(self, num: int) -> None:
        # 먼저 max_heap에 넣고, 조정
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heappop(self.max_heap))
        # max_heap에 원소가 1개 더 들어가도록 함.
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        # 원소 갯수가 even인 경우
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else: # 원소 갯수가 odd인 경우
            return float(-self.max_heap[0])
    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()