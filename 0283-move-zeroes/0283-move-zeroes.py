class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 이러면 non-zero 갯수만큼만 연산.. 최적해.
        last_non_zero_index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[last_non_zero_index], nums[i] = nums[i], nums[last_non_zero_index]
                last_non_zero_index += 1