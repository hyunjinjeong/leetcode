class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 1. one-liner ㅎㅎ
        # return [tup[0] for tup in collections.Counter(nums).most_common(k)]
    
#         # 2. 표준 방법. heap을 사용하면 된다!
#         counter = collections.Counter(nums) # O(N)
#         heap = []
        
#         for num in counter: # O(NlogK)
#             count = counter[num]
#             heapq.heappush(heap, (count, num))
#             if len(heap) == k + 1:
#                 heapq.heappop(heap)
        
#         return [tup[1] for tup in heap] # O(K)
    
#         counter = collections.Counter(nums) # O(N)
#         heap = [(-count, num) for num, count in counter.items()] # O(N)
#         heapq.heapify(heap) # O(N)
        
#         ans = []
#         for _ in range(k): # O(KlogN)
#             ans.append(heapq.heappop(heap)[1])
        
#         return ans
        # 3. bucket sort를 이용하면 O(N)에 가능
        counter = collections.Counter(nums)
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in counter.items():
            bucket[freq].append(num)
        
        ans = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans