import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 1. one-liner ㅎㅎ
        # return [tup[0] for tup in collections.Counter(nums).most_common(k)]
    
        # 2. 표준 방법. heap을 사용하면 된다!
        counter = collections.Counter(nums)
        heap = []
        # min heap 을 사용하면 O(nlogk)가 될 것 같은데?
        for num in counter:
            count = counter[num]
            heapq.heappush(heap, (count, num))
            if len(heap) == k + 1:
                heapq.heappop(heap)
        
        return [tup[1] for tup in heap]