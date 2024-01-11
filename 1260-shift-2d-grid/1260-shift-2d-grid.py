class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 예시로 식 계산해보면 i = (i + (j + k) // n) % m, j = (j + k) % n 으로 정리되는 듯?
        M, N = len(grid), len(grid[0])
        pushed_grid = [[0] * N for _ in range(M)]
        
        k = k % (M * N)
        for i in range(M):
            for j in range(N):
                pushed_i, pushed_j = (i + (j + k) // N) % M, (j + k) % N
                pushed_grid[pushed_i][pushed_j] = grid[i][j]
        
        return pushed_grid