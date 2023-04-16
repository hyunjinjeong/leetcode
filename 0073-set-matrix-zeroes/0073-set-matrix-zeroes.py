class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_has_zero, first_col_has_zero = False, False
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        
        # 0번째 row, col에 기록해두기
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # 0부터 보면 덮어씌워져서 1부터 기록. 어차피 0번째는 위에서 0으로 해놓음.
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0
        
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(1, len(matrix[0])):
                    matrix[r][c] = 0
        
        if first_row_has_zero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if first_col_has_zero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
                
        
            