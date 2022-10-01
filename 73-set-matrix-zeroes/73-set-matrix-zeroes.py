class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 일단 naive 하게 가보자
        len_row, len_col = len(matrix), len(matrix[0])
        zero_rows, zero_cols = [False] * len_row, [False] * len_col
        
        # 0 있으면 체크
        for r in range(len_row):
            for c in range(len_col):
                if matrix[r][c] == 0:
                    zero_rows[r] = True
                    zero_cols[c] = True
        
        # True로 찍힌 애들은 다 0으로 만들어 줌
        for r in range(len_row):
            for c in range(len_col):
                if zero_rows[r] or zero_cols[c]:
                    matrix[r][c] = 0
            