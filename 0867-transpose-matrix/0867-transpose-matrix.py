class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])

        res = [[0] * M for _ in range(N)]
        
        for i in range(M):
            for j in range(N):
                res[j][i] = matrix[i][j]
        
        return res