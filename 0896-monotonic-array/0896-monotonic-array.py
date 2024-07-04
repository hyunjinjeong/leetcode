class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing, is_decreasing = False, False

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] > nums[i-1]:
                if is_increasing: continue
                if is_decreasing: return False
                is_increasing = True
            if nums[i] < nums[i-1]:
                if is_decreasing: continue
                if is_increasing: return False
                is_decreasing = True
        
        return True