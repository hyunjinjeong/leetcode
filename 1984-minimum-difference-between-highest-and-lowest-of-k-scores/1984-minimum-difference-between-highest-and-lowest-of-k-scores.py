class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # easy니까 sorting?
        nums.sort()
        ans = float("inf")

        for i in range(k - 1, len(nums)):
            diff = nums[i] - nums[i - k + 1]
            ans = min(diff, ans)
        
        return ans if ans != float("inf") else 0