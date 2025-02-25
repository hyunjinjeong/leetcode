class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # 이거 그래프 같은데?
        # 그래프를 만든 다음에 BFS든 다익스트라든 돌려서 최단거리를 찾으면 됨. 일단 간단하게 BFS로...
        # N = len(grid)

        # graph = collections.defaultdict(list)
        # for r in range(1, N):
        #     for c in range(N):
        #         for new_col in range(N):
        #             if new_col != c:
        #                 graph[(r - 1, c)].append((r, new_col, grid[r][new_col]))
        
        # q = collections.deque()
        # for c in range(N):
        #     q.append((0, c, grid[0][c]))
        
        # res = float("inf")
        # while q:
        #     r, c, path_sum = q.popleft()
        #     if r == N - 1: # end
        #         res = min(path_sum, res)
            
        #     for adj_r, adj_c, num in graph[(r, c)]:
        #         q.append((adj_r, adj_c, path_sum + num))
        
        # return res

        # 방법은 맞는데 MLE 뜸. 더 최적화하면 되려나? DP를 쓰라는데.. DP도 되긴 하겠다
        N = len(grid)

        def get_min_in_prev_row(r, c):
            res = float("inf")
            for prev_c in range(N):
                if prev_c == c:
                    continue
                res = min(grid[r - 1][prev_c], res)
            return res

        for r in range(1, N):
            for c in range(N):
                grid[r][c] += get_min_in_prev_row(r, c)
        
        return min(grid[N - 1])