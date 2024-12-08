class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        def bisect_left(target):
            START = 0
            left, right = 0, len(jobs)
            
            while left < right:
                mid = (left + right) // 2
                if jobs[mid][START] >= target:
                    right = mid
                else:
                    left = mid + 1
            
            return left

        START, END = 0, 1
        
        jobs = sorted(zip(startTime, endTime))
        dp = [0] * (len(jobs) + 1)
        
        for i in range(len(jobs) - 1, -1, -1):
            # 
            k = bisect_left(jobs[i][END])
            dp[i] = max(profit[i] + dp[k], dp[i+1])
        
        return dp[0]
    