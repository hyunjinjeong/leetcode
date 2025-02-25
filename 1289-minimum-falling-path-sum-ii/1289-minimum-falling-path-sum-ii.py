class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # 그래프인가? 그래프를 만든 다음에 BFS든 다익스트라든 돌려서 최단거리를 찾으면 됨. 일단 간단하게 BFS로...
        # 아 근데 음수가 있어서 안되는구나. 그럼 걍 DP로...
        N = len(grid)

        def get_first_two_minimum_indices(row):
            first, second = None, None
            for col in range(N):
                if first is None:
                    first = col
                elif second is None:
                    if grid[row][col] < grid[row][first]:
                        first, second = col, first
                    else:
                        second = col
                elif grid[row][col] < grid[row][first]:
                    first, second = col, first
                elif grid[row][col] < grid[row][second]:
                    second = col
            
            return first, second

        for row in range(1, N):
            first_min_index, second_min_index = get_first_two_minimum_indices(row - 1)
            for col in range(N):
                if col != first_min_index:
                    grid[row][col] += grid[row - 1][first_min_index]
                else:
                    grid[row][col] += grid[row - 1][second_min_index]
        
        return min(grid[N - 1])