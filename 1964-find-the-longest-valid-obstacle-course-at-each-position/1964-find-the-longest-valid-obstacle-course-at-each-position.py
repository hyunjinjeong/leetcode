class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # 0 ~ i 사이에서 최대 높이가 obstacles[i]인 LIS를 찾아야 함
        # 0 ~ (i - 1) 사이에서 obstacles[i]보다 값이 같거나 작은 수로만 이루어진 LIS를 찾는 문제로 치환되나?
        # 그럼 그 LIS의 길이 + 1 == res[i]
        # 흠 답은 맞는데 TLE가 뜬다.

        N = len(obstacles)

        def bisect_right(arr, target):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] > target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        # dp[k]는 길이가 k인 코스의 마지막 장애물 값으로 가능한 최솟값
        dp = []
        res = []
        for num in obstacles:
            i = bisect_right(dp, num)
            
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
            
            res.append(i + 1)
        
        return res