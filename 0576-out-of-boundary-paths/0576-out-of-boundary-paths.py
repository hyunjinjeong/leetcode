class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 100% dp
        # base 조건은... m, n이 밖에 나가면? 왜냐면 모서리에 있어도 move가 남아 있으면 여기저기로 갈 수 있음
        # 그리고 maxMove가 0일 때겠지..
        # 시작지점에서부터 maxMove를 하나씩 빼면서 값을 더해가야 하는데
        # 아 그런데 이전에 갔던 지점으로 다시 되돌아올 수가 있네..? 이 경우는 어떻게 처리해주지
        # 실제로 되돌아가진 않을 것 같고 식을 쓰지 않을까?
        # 예를 들어서 단순히 왔다갔다는 2를 빼면 됨. 아니면 실제로 되돌아가기..?
        # left_move가 있으니까 구분이 될 듯?
        MOD = 10 ** 9 + 7

        # @cache
        # def dfs(r, c, move_left):
        #     if r < 0 or r >= m or c < 0 or c >= n:
        #         return 1
        #     if move_left == 0:
        #         return 0
            
        #     up = dfs(r - 1, c, move_left - 1)
        #     right = dfs(r, c + 1, move_left - 1)
        #     down = dfs(r + 1, c, move_left - 1)
        #     left = dfs(r, c - 1, move_left - 1)
        #     return (((((up + right) % MOD) + down) % MOD) + left) % MOD
        
        # return dfs(startRow, startColumn, maxMove)

        # bottom-up으로...
        dp = [[0] * n for _ in range(m)]

        for move in range(maxMove): # move는 loop를 도는 역할 말고는 하는게 없군
            tmp_dp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    up = dp[r - 1][c] if r > 0 else 1
                    right = dp[r][c + 1] if c < n - 1 else 1
                    down = dp[r + 1][c] if r < m - 1 else 1
                    left = dp[r][c - 1] if c > 0 else 1
                    tmp_dp[r][c] = ((up + right) % MOD + (down + left) % MOD) % MOD
            dp = tmp_dp
        
        return dp[startRow][startColumn]