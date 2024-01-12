class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_dup_index = 0

        # nums[i+1], nums[i]가 같은지 유무로 판단?
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                if i + 1 < len(nums) and nums[i+1] == nums[i]:
                    nums[non_dup_index] = nums[i]
                    nums[non_dup_index + 1] = nums[i]
                    non_dup_index += 2
                else:
                    nums[non_dup_index] = nums[i]
                    non_dup_index += 1

        return non_dup_index