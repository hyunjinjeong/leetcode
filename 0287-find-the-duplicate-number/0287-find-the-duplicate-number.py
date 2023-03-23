class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         # 1. 일단 O(n) 공간 쓰는 방법으로.. 시간은 O(n)
#         result = -1
#         dt = {}
#         for num in nums:
#             if num in dt:
#                 result = num
#                 break
#             else:
#                 dt[num] = 0
        
#         return result
#         # 2. 공간을 O(1)로 맞추면... 이건 시간은 O(n^2). TLE 뜬다.
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return nums[i]
#         # 3. binary search를 이용하면 시간이 O(nlogn)으로 준다.
#         # count가 mid보다 크면 중복이 있다는 소리... 그래서 이걸 가지고 찾는다.
#         # 중복이 없으면 1,2,3,4에서 예를들어 2보다 같거나 작은 수는 2개. 즉 mid랑 같아짐
#         # 'low' and 'high' represent the range of values of the target
#         low, high = 1, len(nums) - 1
#         while low <= high:
#             mid = (low + high) // 2
#             count = 0

#             # Count how many numbers are less than or equal to 'mid'
#             count = sum(num <= mid for num in nums)
#             if count > mid:
#                 duplicate = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
                
#         return duplicate
        # 4. 플로이드의 토끼와 거북이 이용. (Floyd's Tortoise and Hare)
        # 시간은 O(n), 공간은 O(1). 얘만 결국 모든 constraints를 만족하네...
        # Phase 1: Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Phase 2: Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare