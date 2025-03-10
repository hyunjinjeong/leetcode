class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp인데...
        # n == 1 -> 당연히 5고
        # n == 2 -> 앞의 모음을 기준으로 생각할지 뒤에 붙일 모음을 기준으로 생각할지 정하자
        # 앞을 기준으로 하면
        # a 뒤에는 e만 올 수 있음
        # e 뒤에는 a, i
        # i 뒤에는 a, e, o, u
        # o 뒤에는 i, u
        # u 뒤에는 a
        # 뭔가 복잡하다... 뒤의 모음을 기준으로 생각하면?
        # a. 앞에 올 수 있는건 e, i, u
        # e. a, i
        # i. e, o
        # o. i
        # u. i, o.
        # 바로 이전 상태만 참고하니까 길이 5짜리 배열로 구현할 수 있을 듯
        MOD = 10 ** 9 + 7

        dp = [1] * 5
        for num in range(1, n):
            new_dp = [1] * 5
            for index in range(5):
                if index == 0: # a
                    new_dp[index] = (dp[1] + (dp[2] + dp[4]) % MOD) % MOD
                elif index == 1: # e
                    new_dp[index] = (dp[0] + dp[2]) % MOD
                elif index == 2: # i
                    new_dp[index] = (dp[1] + dp[3]) % MOD
                elif index == 3: # o
                    new_dp[index] = dp[2]
                elif index == 4: # u
                    new_dp[index] = (dp[2] + dp[3]) % MOD
            dp = new_dp
        
        res = 0
        for index in range(5):
            res = (res + dp[index]) % MOD
        return res
        