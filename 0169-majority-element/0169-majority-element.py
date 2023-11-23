class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         # 1. O(n) 공간 쓰는건 쉬움
#         counter = collections.defaultdict(int)
        
#         for num in nums:
#             counter[num] += 1
#             if counter[num] > len(nums) // 2:
#                 return num

        # 2. O(1) 공간은?
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate