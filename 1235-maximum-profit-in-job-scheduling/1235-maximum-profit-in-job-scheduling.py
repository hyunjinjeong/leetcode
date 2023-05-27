class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        START, END, PROFIT = 0, 1, 2
        
        # startTime을 기준으로 정렬
        jobs = sorted(zip(startTime, endTime, profit))
        dp = [0] * (len(jobs) + 1)
        
        for i in range(len(jobs)-1, -1, -1):
            # binary search를 이용해서, 현재 job의 endTime보다 큰 startTime을 가진 job을 찾음. 맨 왼쪽.
            k = self.bisect_left(jobs, jobs[i][END])
            dp[i] = max(jobs[i][PROFIT] + dp[k], dp[i+1])
        
        return dp[0]
    
    def bisect_left(self, jobs, target):
        START = 0
        left, right = 0, len(jobs)
        
        while left < right:
            mid = (left + right) // 2
            if jobs[mid][START] < target:
                left = mid + 1
            else:
                right = mid
        
        return left