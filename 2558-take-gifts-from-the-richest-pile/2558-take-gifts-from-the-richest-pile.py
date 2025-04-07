class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heap.append(-1 * gift)
        heapq.heapify(heap)

        seconds = 0
        while seconds < k:
            pile = -1 * heapq.heappop(heap)
            heapq.heappush(heap, -1 * math.floor(math.sqrt(pile)))

            seconds += 1
        
        return -1 * sum(heap)
