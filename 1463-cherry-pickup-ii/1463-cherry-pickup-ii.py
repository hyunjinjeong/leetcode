class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # brute force로 접근하면 로봇 하나당 매번 3개의 선택이 가능하니 O(3^n)이고, 로봇이 2개니까 O(2 * 3^n)인가?
        # 당연히 안 될 거고 DP로 풀어야 할 것 같음
        # 문제는 로봇 하나가 지나가면 체리를 다 수집한다는 점인데
        # 따로따로 계산해서 더하는 방식이 아니라 매번 같이 계산해야 할 것 같음
        
        @cache
        def dfs(r, c1, c2):
            if not (0 <= r < ROWS and 0 <= c1 < COLS and 0 <= c2 < COLS):
                return 0
            
            res = grid[r][c1]
            if c1 != c2:
                res += grid[r][c2]
            
            # 총 9가지 경우의 수가 있음
            sub = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    sub = max(dfs(r + 1, c1 + i, c2 + j), sub)
            
            return res + sub
        
        return dfs(0, 0, COLS - 1)
            