class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         # 일단 naive한 방법... 정렬한 다음에 이렇게 비교하면 된당. 공간은 O(1) 시간은 O(nlogn)
#         nums.sort()
        
#         for i in range(len(nums)):
#             if i != nums[i]:
#                 return i
        
#         return len(nums)
    
        # Follow-up으로 O(1) 공간과 O(n) 시간 복잡도로 해결해야 함.
        # 일단 O(n) 공간 O(n) 시간은 set 써서 이런 식으로 된당.
        s = set([i for i in range(len(nums)+1)])
        s2 = set(nums)
        
        # 원소 한개만 남았을 거
        diff = s - s2
        
        return list(diff)[0]
        
        
        