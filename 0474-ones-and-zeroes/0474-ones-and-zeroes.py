class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # largest subset이라는게 숫자의 합이 아니고 subset의 갯수를 말함
        # 일단 decision tree.. 느낌으로 풀어보자
        # i번째가 있으면 i를 포함하거나, 포함하지 않거나.
        # 반대로 그냥 전체 subset을 다 구해서 조건에 맞는 subset들만 필터링해서 보면 됨
        # TLE가 뜨는데.. DP인 것 같음. 어떻게 DP로 전환하지. curr를 안 쓰도록 해보자.
        # 다음은 bottom up
        def count_zeros(s):
            count = 0
            for c in s:
                if c == "0":
                    count += 1
            return count
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros = count_zeros(s)
            ones = len(s) - zeros

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        return dp[m][n]