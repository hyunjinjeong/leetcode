class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        
        for i, num in enumerate(nums):
            if num in dt:
                return [dt[num], i]
            else:
                dt[target - num] = i