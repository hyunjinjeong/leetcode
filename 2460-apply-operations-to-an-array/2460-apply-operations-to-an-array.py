class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        i, j = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                i += 1
                continue

            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                res[j] = nums[i] * 2
                i += 2
            else:
                res[j] = nums[i]
                i += 1
            j += 1
        
        return res