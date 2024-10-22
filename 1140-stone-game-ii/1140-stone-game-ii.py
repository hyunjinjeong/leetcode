class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp인데..
        # piles 길이는 최대 100.
        # X 값에 따라서 몇 개의 이전 상태를 봐야 하는지가 정해지는데 X가 <= 100일거니까
        # 100 * 100 배열로 만들면 되려나?
        # M 값에 따라서 정해지는구나
        # 일단 top down으로 해보자
        # alice와 bob을 나눠서 계산해야 하는데..?

        @cache
        def dfs(i, m, is_alice):
            if i >= len(piles):
                return 0
            
            res = 0 if is_alice else float("inf")
            for x in range(1, m * 2 + 1):
                if is_alice:
                    res = max(res, sum(piles[i:i + x]) + dfs(i + x, max(x, m), False))
                else:
                    res = min(res, dfs(i + x, max(x, m), True))
            
            return res
        
        return dfs(0, 1, True)