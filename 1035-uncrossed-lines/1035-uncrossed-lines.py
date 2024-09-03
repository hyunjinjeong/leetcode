class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 규칙을 생각해보자
        # 일단 nums1 - nums2를 이었을 때... 
        # index를 각각 i, j라고 하면 그 사이 범위의 인덱스 (inclusive)는 연결할 수가 없음
        # 즉 ~i-1, j+1~ 범위로 다시 연결 가능...
        # LCS랑 똑같은 문제였다!
        # cache = {}

        # def dfs(i, j):
        #     if i >= len(nums1) or j >= len(nums2):
        #         return 0
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     if nums1[i] == nums2[j]:
        #         res = 1 + dfs(i + 1, j + 1)
        #     else:
        #         res = max(dfs(i, j + 1), dfs(i + 1, j))
            
        #     cache[(i, j)] = res
        #     return res
        
        # return dfs(0, 0)
        N, M = len(nums1), len(nums2)
        # dp = [[0] * (M + 1) for _ in range(N + 1)]
        prev_dp = [0] * (M + 1)

        for i in range(N - 1, -1, -1):
            dp = [0] * (M + 1)
            for j in range(M - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    # dp[i][j] = 1 + dp[i + 1][j + 1]
                    dp[j] = 1 + prev_dp[j + 1]
                else:
                    # dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                    dp[j] = max(dp[j + 1], prev_dp[j])
            prev_dp = dp
        
        # return dp[0][0]
        return prev_dp[0]