class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_dup_index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[non_dup_index] = nums[i]
                non_dup_index += 1
        
        return non_dup_index