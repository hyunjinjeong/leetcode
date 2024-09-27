class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = []
        for i in range(len(nums) - n):
            new_nums.append(nums[i])
            new_nums.append(nums[i + n])
        return new_nums