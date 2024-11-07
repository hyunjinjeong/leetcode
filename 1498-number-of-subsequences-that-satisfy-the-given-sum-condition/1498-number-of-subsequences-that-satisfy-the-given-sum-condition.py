class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7

        nums.sort()
        res = 0

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + (1 << (right - left))) % MOD
                left += 1
            else:
                right -= 1

        return res