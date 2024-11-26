class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = nums[:]

        q = collections.deque()
        for i in range(1, N):
            # Build decreasing deque
            if q and q[0] == i - k - 1:
                q.popleft()

            while q and dp[q[-1]] < dp[i - 1]:
                q.pop()
            
            q.append(i - 1)
            
            max_prev = 0
            if q:
                max_prev = dp[q[0]]
            dp[i] = max(dp[i], nums[i] + max_prev)

        return max(dp)