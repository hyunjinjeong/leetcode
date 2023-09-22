class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # N = len(nums)
        # # dp
        # dp = [1] * N

        # for i in range(N):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[j] + 1, dp[i])
            
        # return max(dp)

        # dp 2. O(nlogn).
        N = len(nums)
        def bisect_left(val, arr):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        dp = [nums[0]]
        for num in nums:
            if num > dp[-1]:
                dp.append(num)
            else:
                i = bisect_left(num, dp)
                dp[i] = num

        return len(dp)