class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])

        zero_in_first_row, zero_in_first_col = False, False
        for i in range(M):
            if matrix[i][0] == 0:
                zero_in_first_col = True
                break
        for i in range(N):
            if matrix[0][i] == 0:
                zero_in_first_row = True
                break
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, M):
            if matrix[i][0] == 0:
                for j in range(1, N):
                    matrix[i][j] = 0
        for j in range(1, N):
            if matrix[0][j] == 0:
                for i in range(1, M):
                    matrix[i][j] = 0
        
        if zero_in_first_row:
            for i in range(N):
                matrix[0][i] = 0
        if zero_in_first_col:
            for i in range(M):
                matrix[i][0] = 0