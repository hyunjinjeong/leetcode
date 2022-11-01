import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 1. one-liner ㅎㅎ
        # return [tup[0] for tup in collections.Counter(nums).most_common(k)]
    
        # 2. 표준 방법. heap을 사용하면 된다!
        counter = collections.Counter(nums)
        heap = []
        for num in counter:
            count = counter[num]
            heapq.heappush(heap, (-count, num)) # min heap이므로 max heap으로 만들어주기 위해. 0번째 기준으로 정렬함
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result