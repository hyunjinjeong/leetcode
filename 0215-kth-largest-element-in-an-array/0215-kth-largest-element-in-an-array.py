class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap을 사용한다면? => O(n)을 넘어서 안됨
        # sort도 당연히 안되고
        # quickselect를 사용해야 한다...
        # 1. 일단 min heap 버전
        # 시간은 nlogk? 공간은 O(k).
        heap = []
        # 먼저 k개만큼 넣어서 크기 k로 만들어주고...
        for i in range(k):
            heapq.heappush(heap, nums[i])
        # 다음엔 하나씩 넣고 뺴고 하다보면 작은 순서로 쭉쭉 빠져나가니까 k번째 큰 수가 남음.
        for i in range(k, len(nums)):
            heapq.heappushpop(heap, nums[i])
        
        # 이제 root가 k번째 큰 원소
        return heapq.heappop(heap)
        
        # 2. quickselect 버전