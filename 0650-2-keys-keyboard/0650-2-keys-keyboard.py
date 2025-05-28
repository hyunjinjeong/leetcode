class Solution:
    def minSteps(self, n: int) -> int:
        # 3 = 1 + 1 + 1 or 2 + 1
        # 처음에는 copy밖에 못하니까..
        # 1 다음에는 무조건 2가 된다.
        # 그래서 3이면 다시 paste 해서 A copy -> A paste -> A paste.
        # 소수가 아니면 나눠지는 수가 있어서, 나눈 수를 쓸지 정할 수 있겠구만. 소수면 n개고

        # 10이면 2 * 5도 되고 5 * 2도 되는데 둘이 결과가 같으려나? 똑같네
        # ops(quotient) + n // quotient 수만큼 들어간다.

        # cache = {}
        # def dfs(num):
        #     if num == 1:
        #         return 0
        #     if num in cache:
        #         return num
            
        #     ops = num
        #     for quotient in range(2, int(num ** 1/2) + 1):
        #         if num % quotient != 0:
        #             continue
        #         ops = min(ops, dfs(quotient) + num // quotient)

        #     return ops
        
        # return dfs(n)

        dp = [1001] * (n + 1)
        dp[0] = dp[1] = 0

        for num in range(2, n + 1):
            for quotient in range(1, int(num ** 1/2) + 1):
                if num % quotient != 0:
                    continue
                dp[num] = min(dp[num], dp[quotient] + num // quotient)
        
        return dp[n]
