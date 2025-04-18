class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                for j in range(i, i + 3):
                    nums[j] ^= 1 # 1 ^ 1 = 0, 0 ^ 1 = 1
                ops += 1
        return ops if nums[-1] == nums[-2] == 1 else -1
