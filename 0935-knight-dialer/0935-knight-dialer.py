class Solution:
    def knightDialer(self, n: int) -> int:
        # dp 겠지? 움직임을 수식화할 수 있나
        MOD = 10 ** 9 + 7
        can_move = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]   
        }

        # @cache
        # def dfs(num, count):
        #     if count == n:
        #         return 1

        #     res = 0
        #     for next_num in can_move[num]:           
        #         res = (res + dfs(next_num, count + 1)) % MOD
            
        #     return res

        # res = 0
        # for num in range(10):
        #     res = (res + dfs(num, 1)) % MOD
        
        # return res

        # bottom-up
        dp = [[0] * 10 for _ in range(n)]
        dp[0] = [1] * 10

        for count in range(1, n):
            for num in range(10):
                for next_num in can_move[num]:
                    dp[count][next_num] = (dp[count][next_num] + dp[count - 1][num]) % MOD
        
        return sum(dp[-1]) % MOD