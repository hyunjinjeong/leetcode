class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 홀수 index 숫자는 양 옆의 숫자보다 높아야 함
        # greedy로 가능하네..
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]
                or i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]