class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # 일단 0번째 row의 1이 많을 수록 좋은데
        # 0 -> 1 -> 2... 이런 순이고
        # 아 전체 max가 아니라 각 row의 max구나
        # 그러면 0번째 col이 다 1이 되도록 row를 뒤집어 주고
        # 1번째 col부터는 1이 많도록..
        R, C = len(grid), len(grid[0])

        def col_one_count(c):
            count = 0
            for r in range(0, R):
                if grid[r][c] == 1:
                    count += 1
            return count

        for r in range(R):
            if grid[r][0] == 0:
                for c in range(C):
                    grid[r][c] ^= 1

        for c in range(1, C):
            if col_one_count(c) <= R // 2:
                for r in range(R):
                    grid[r][c] ^= 1
        
        res = 0
        for r in range(R):
            curr = 0
            for c in range(C):
                curr = curr * 2 + grid[r][c]
            res += curr
        return res