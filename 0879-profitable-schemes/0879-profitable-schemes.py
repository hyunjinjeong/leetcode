class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 순서는 상관 없음. 0, 1, 2를 하든 2, 1, 0을 하든...
        # pick & not pick DP? 근데 시간 복잡도가 2^100이라 TLE가 뜰 것 같음
        # 어떤 선택을 할 때... curr_profit을 알아야 하고 또 curr_members를 알아야 함

        # 1번 예제에서
        # 0 -> profit 2, members 2: X
        # 0 1 -> profits 5, members 4: O
        # 1 -> profit 3, members 2: O
        # 이런 식인데...
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i, curr_members, curr_profit):
            if i == len(group):
                return 1 if curr_profit >= minProfit else 0

            # not pick
            res = dfs(i + 1, curr_members, curr_profit)
            if curr_members + group[i] <= n: # pick
                new_profit = min(curr_profit + profit[i], minProfit)
                res += dfs(i + 1, curr_members + group[i], new_profit)
            
            return res % MOD
        
        return dfs(0, 0, 0)