class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)

        res = 0
        for i in range(N):
            res += mat[i][i]
            # 0, n-1에서 n-1, 0까지..
            res += mat[i][N - 1 - i]
        
        if N % 2 == 1:
            res -= mat[N // 2][N // 2]
        
        return res