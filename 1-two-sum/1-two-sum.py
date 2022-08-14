class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        
        for i in range(len(nums)):
            num = nums[i]
            num_to_find = target - num
            
            if num_to_find in dt:
                return [dt[num_to_find], i]
            
            dt[num] = i