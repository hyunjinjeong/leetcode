class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [0] * N

        q = collections.deque()
        for i in range(N):
            # Build decreasing deque and calculate dp[i]
            if q and q[0] == i - k - 1:
                q.popleft()
        
            max_prev = dp[q[0]] if q else 0
            dp[i] = nums[i] + max_prev

            while q and dp[q[-1]] < dp[i]:
                q.pop()

            if dp[i] > 0:
                q.append(i)

        return max(dp)