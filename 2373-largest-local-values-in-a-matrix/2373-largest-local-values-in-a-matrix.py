class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # 무슨 자료구조가 좋을까...
        # n <= 100이넹. 그러면 매번 계산해도 큰 문제는 없을 듯?
        N = len(grid)
        res = [[0] * (N - 2) for _ in range(N - 2)]

        def get_max(i, j):
            res = 0
            for x in range(3):
                for y in range(3):
                    res = max(res, grid[i + x][j + y])
            return res
        
        for i in range(N - 2):
            for j in range(N - 2):
                res[i][j] = get_max(i, j)
        
        return res