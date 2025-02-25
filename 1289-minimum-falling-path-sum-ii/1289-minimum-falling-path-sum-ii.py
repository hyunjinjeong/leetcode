class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # 그래프인가? 그래프를 만든 다음에 BFS든 다익스트라든 돌려서 최단거리를 찾으면 됨. 일단 간단하게 BFS로...
        # 아 근데 음수가 있어서 안되는구나
        N = len(grid)

        # def get_first_two_minimum_indices(row):
        #     first, second = float("inf"), float("inf")
        #     for col in range(N):



        for r in range(1, N):
            for c in range(N):
                grid[r][c] += min(grid[r - 1][k] for k in range(N) if k != c)
        
        return min(grid[N - 1])