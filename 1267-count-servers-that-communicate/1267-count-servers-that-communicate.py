class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # 흠 brute force 말고 다른 방법이 있는건가
        # ㅇㅋ row나 col 수를 저장한 다음에 돌면서 max(row, col) >= 2 이면 된다
        M, N = len(grid), len(grid[0])

        rows = [0] * M
        cols = [0] * N

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and max(rows[i], cols[j]) >= 2:
                    res += 1
        
        return res
