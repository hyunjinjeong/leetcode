class Solution:
    def minDays(self, n: int) -> int:
        # 매일 최대 3가지 선택이 가능함
        # 1. 오렌지 1개 먹기 -> n - 1
        # 2. 2로 나누어지면 n // 2 개 먹기 -> n // 2
        # 3. 3으로 나누어지면 2 * n // 3 개 먹기 -> n // 3
        # dp로 안되나?

        # 아마 i - 1 케이스를 빼야할 것 같음
        @cache
        def dfs(oranges):
            if oranges <= 1:
                return oranges

            return min(1 + oranges % 2 + dfs(oranges // 2), 1 + oranges % 3 + dfs(oranges // 3))
        
        return dfs(n)