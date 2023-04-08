class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
#         # 1. 일단 min heap 버전
#         # 시간은 nlogk? 공간은 O(k).
#         heap = []
#         # 먼저 k개만큼 넣어서 크기 k로 만들어주고...
#         for i in range(k):
#             heapq.heappush(heap, nums[i])
#         # 다음엔 하나씩 넣고 뺴고 하다보면 작은 순서로 쭉쭉 빠져나가니까 k번째 큰 수가 남음.
#         for i in range(k, len(nums)):
#             heapq.heappushpop(heap, nums[i])
        
#         # 이제 root가 k번째 큰 원소
#         return heapq.heappop(heap)
        
        # 2. quickselect 버전
        return self.quick_select(nums, 0, len(nums)-1, k)
    
    def quick_select(self, nums, start, end, k):
        
        def partition(left, right):
            pivot_index = random.randint(left, right)
            # swap을 쉽게 하기 위해 맨 마지막으로 보냄
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            
            pivot = nums[right]
            for i in range(left, right+1):
                if nums[i] >= pivot: # kth largest니까 pivot보다 큰 친구들을 왼쪽으로 보냄
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            
            # 이 시점에서 left는 pivot보다 작은 첫 번째 원소 위치 (swap 후 +1 되므로)
            # 따라서 -1을 해야 pivot의 위치가 됨
            return left - 1
        
        l, r = 0, len(nums)-1
        while True:
            pivot_index = partition(l, r)
            
            # zero-based index니까 k-1 사용.
            if pivot_index == k-1:
                return nums[pivot_index]
            
            if pivot_index < k-1:
                l = pivot_index + 1
            else:
                r = pivot_index - 1