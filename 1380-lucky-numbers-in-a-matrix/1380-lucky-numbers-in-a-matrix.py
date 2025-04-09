class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])

        row_min, col_max = [100000] * M, [0] * N
        for i in range(M):
            for j in range(N):
                num = matrix[i][j]
                row_min[i] = min(row_min[i], num)
                col_max[j] = max(col_max[j], num)
        
        res = []
        for i in range(M):
            for j in range(N):
                num = matrix[i][j]
                if num == row_min[i] and num == col_max[j]:
                    res.append(num)
        return res